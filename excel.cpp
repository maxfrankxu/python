//  Excel.cpp
//
//  Created 22/12
// 
//
 
#include <iostream>
#include <string>
 
#include "Excel.h"
#include "cocos2d.h"
 
#include "external/tinyxml2/tinyxml2.h"
 
using namespace tinyxml2;
using namespace std;
 
unsigned char* getFileDataFromZip(const std::string& zipFilePath, const std::string& filename, ssize_t *size)
{
    return cocos2d::FileUtils::getInstance()->getFileDataFromZip(zipFilePath, filename, size);
}
 
void deleteNum( std::string &content)
{
    string::iterator t = content.begin();
    while(t != content.end())
    {
        if(*t >= '0' && *t <= '9')
        {
           content.erase(t);
        }
        else
        {
            t++;
        }
    }
}
int getColIndex(std::string &content)
{
    auto returnValue = 0;
    for (auto i =0; i < content.length(); i++)
    {
        char n = content[i];
        auto cValue = n - 64;
        returnValue *= 26;
        returnValue += cValue;
    }
    return returnValue - 1;
}
 
Excel::Excel()
:_excelFilePath("")
{
     
}
 
bool Excel::parseExcelFile(const std::string &ilepath, int sheetIndex)
{
    _excelFilePath = ilepath;
    excelHash.clear();
     
    char xml_file[256] = {0};
    sprintf(xml_file, "xl/worksheets/sheet%d.xml",sheetIndex+1);
    ssize_t size;
     
    auto fileData = getFileDataFromZip(_excelFilePath, xml_file, &size);
    if (!fileData)
    {
        CCLOG(ilepath.c_str(), "The excel file is not exist£¡");
        return false;
    }
    auto valueArray = std::move(_getValueArray());
 
    tinyxml2::XMLDocument doc;
 
    doc.Parse((const char*)fileData,size);
     
    XMLElement *root = doc.RootElement();
     
    XMLElement * sheetDataElement = root->FirstChildElement("sheetData");
    XMLElement * rowElement =sheetDataElement->FirstChildElement("row");
     
    while (rowElement)
    {
        LineInfo lineInfo;
        auto rowIndex = atoi(rowElement->Attribute("r")) - 1;
        lineInfo.lineIndex = rowIndex;
        std::vector<std::string> &rowArray = lineInfo.array;
        auto cElement = rowElement->FirstChildElement("c");
        while (cElement)
        {
            std::string cc = cElement->Attribute("r");
            deleteNum(cc);
            auto colIndex  = getColIndex( cc );
            std::string t = "";
            std::string v = "";
 
            if (cElement->Attribute("t"))
            {
                t = cElement->Attribute("t");
            }
            auto vElement = cElement->FirstChildElement("v");
            if (vElement)
            {
                v = vElement->GetText();
            }
            if (rowArray.size() < colIndex)
            {
                int len = rowArray.size();
                for (auto i = 0;i < colIndex - len;i++)
                {
                    rowArray.push_back(""); //
                }
            }
            if (t == "s")
            {
                rowArray.push_back(valueArray[atoi(v.c_str())]);
            }
            else
            {
                rowArray.push_back(v);
            }
            cElement = cElement->NextSiblingElement("c");
        }
        auto bb = false;
        for (auto iii : rowArray)
        {
            if (iii.length() > 1)
            {
                bb = true;
                break;
            }
        }
        if (bb)
        {
            excelHash[rowIndex] = lineInfo;
        }
        rowElement = rowElement->NextSiblingElement("row");
    }
    return true;
}
 
std::vector<std::string> Excel::_getValueArray()
{
    std::vector<std::string> result;
     
    ssize_t size;
    auto fileData = getFileDataFromZip(_excelFilePath,  "xl/sharedStrings.xml", &size);
     
    tinyxml2::XMLDocument doc;
    doc.Parse((const char*)fileData,size);
    XMLElement *root = doc.RootElement();
    XMLElement *siElement = root->FirstChildElement("si");
     
    while (siElement)
    {
        std::string temp = "";
        auto tElement = siElement->FirstChildElement("t");
        while (tElement)
        {
            temp = temp + tElement->GetText();
            tElement = tElement->NextSiblingElement("t");
        }
        result.push_back(temp);
        siElement = siElement->NextSiblingElement("si");
    }
    return result;
}
 
std::vector<LineInfo> Excel::getSheetArray()
{
    std::vector<LineInfo> result;
    for ( auto ite = excelHash.begin();ite != excelHash.end();ite++)
    {
        auto &lineInfo_ = ite->second;
        result.push_back(lineInfo_);
    }
    return result;
}