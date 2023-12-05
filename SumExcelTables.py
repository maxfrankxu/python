import glob
import os

import openpyxl
import csv

TARGET_FILE = glob.glob("日报表/*.xlsx")[-1]


def read_xls_file(file_path=TARGET_FILE):
    """读取xlsx文件并打印
    :param file_path: Excel文件路径
    """
    # 打开Excel文件
    wb = openpyxl.load_workbook(file_path, data_only=True)
    # 打印工作簿名称
    for sheet_name in wb.sheetnames:
        print(sheet_name)
        # 打印单元格内容
        sheet = wb[sheet_name]
        for row in sheet.rows:
            for cell in row:
                print(cell.value, end="\t")
            print()


def get_target_data_list(file_path=TARGET_FILE):
    """
    读取xlsx文件，获得日期、底薪人数、每日总业绩、每日总成本。\n
    :param file_path: Excel文件路径
    :return: date_list: 日期列表; work_people_num_list: 底薪（出勤）人数列表; daily_performance_list: 每日业绩列表; daily_cost_list: 每日成本列表; daily_profit_list: 每日利润列表。
    """
    wb = openpyxl.load_workbook(file_path, data_only=True)  # 打开Excel文件,data_only=True设置取值而非取公式
    date_list = []  # 1. 日期，也是工作簿名称
    work_people_num_list = []  # 2. 工作人数，底薪人数
    daily_performance_list = []  # 3. 每日总业绩列表
    daily_cost_list = []  # 4. 每日成本列表
    daily_profit_list = []  # 5. 每日利润列表
    for sheet_name in wb.sheetnames:
        # 1. 获取日期
        date_ = sheet_name  # 日期名（工作簿名）
        date_list.append(sheet_name)
        print(f"日期：{sheet_name}")  # 打印工作簿名称（日期）

        sheet = wb[sheet_name]  # 获取工作簿
        # 2. 获取每日底薪人数
        one_sheet_work_people_num = sheet['R5'].value  # 一张表（一天）的底薪人数
        print(f"底薪人数：{one_sheet_work_people_num}人")
        work_people_num_list.append(one_sheet_work_people_num)
        # 3. 获取每日总业绩
        one_sheet_daily_performance = sheet['R6'].value  # 一张表（一天）的总业绩
        daily_performance_list.append(one_sheet_daily_performance)
        print(f"每日总业绩：{one_sheet_daily_performance}")
        # 4. 获取每日总成本
        one_sheet_daily_cost = sheet['R7'].value
        daily_cost_list.append(one_sheet_daily_cost)
        print(f"每日总成本：{one_sheet_daily_cost}")

        # 5. 获取每日总利润
        one_sheet_daily_profit = sheet['R8'].value
        daily_profit_list.append(one_sheet_daily_profit)
        print(f"每日利润：{one_sheet_daily_profit}")

        print()
    return date_list, work_people_num_list, daily_performance_list, daily_cost_list, daily_profit_list


def csv_to_excel(csv_filename, excel_filename):
    """
    将csv文件转换为excel文件。\n
    :param csv_filename: 被转换的csv文件的名称。
    :param excel_filename: 目标生成的Excel文件的名称。
    :return:
    """
    # 1. 读取csv文件
    csv_data = []
    with open(csv_filename) as f:
        csv_data = [row for row in csv.reader(f)]
    # 2. 写入Excel文件中
    workbook = openpyxl.workbook.Workbook()
    worksheet = workbook.active
    for row in csv_data:
        worksheet.append(row)
    workbook.save(excel_filename)


def main():
    """过渡函数，作为主函数和其他函数的中介。主要管理和疏通整个代码运行逻辑。
    """
    # 1. 获取日期、底薪人数（出勤的人数）、每日总业绩、每日总成本、每日利润
    date_list, work_people_num_list, daily_performance_list, daily_cost_list, daily_profit_list = get_target_data_list()
    # 2. 将数据按指定格式保存在csv文件中
    date_list_ = [""] + date_list
    work_people_num_list_ = ["底薪人数"] + work_people_num_list
    daily_performance_list_ = ["总业绩"] + daily_performance_list
    daily_cost_list_ = ["总成本"] + daily_cost_list
    daily_profit_list_ = ["利润"] + daily_profit_list
    with open("统计汇总.csv", "w", newline="", encoding="gbk") as f:
        writer = csv.writer(f)
        writer.writerow(date_list_)
        writer.writerow(work_people_num_list_)
        writer.writerow(daily_performance_list_)
        writer.writerow(daily_cost_list_)
        writer.writerow(daily_profit_list_)
    # 3. 将csv文件转换成excel文件
    csv_filename = "统计汇总.csv"
    excel_filename = f"{date_list[0]}到{date_list[-1]}数据统计汇总.xlsx"
    csv_to_excel(csv_filename, excel_filename)
    # 4. 删除csv文件
    os.remove("统计汇总.csv")


if __name__ == "__main__":
    main()
# 　参考相关文章：
# https://zhuanlan.zhihu.com/p/342422919
# https://juejin.cn/post/7109795200611909669

