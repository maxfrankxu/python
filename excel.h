//
//  Excel.h
//  基于com.lipi.excel as3 版本设计
//  Created by howe on 15/5/5.
//    auto excel =  new Excel();
//    bool result = excel->parseExcelFile(filepath, 1);
//    std::vector<LineInfo> arr = std::move( excel->getSheetArray() );
//
 
#ifndef __ModelEditor__Excel__
#define __ModelEditor__Excel__
 
#include <stdio.h>
#include <vector>
#include <map>
 
 
struct LineInfo
{
    int lineIndex;
    std::vector<std::string> array;
};
 
class Excel
{
public:
    Excel();
     
    bool parseExcelFile(const std::string &filepath,int sheetIndex);
     
    std::vector<LineInfo> getSheetArray();
     
private:
    std::vector<std::string> _getValueArray();
private:
    std::map<int,LineInfo> excelHash;
    std::string _excelFilePath;
};
 
#endif /* defined(__ModelEditor__Excel__) */