import openpyxl

# 打开Excel文件
wb = openpyxl.load_workbook('example.xlsx')

# 选择工作表
sheet = wb['Sheet1']

# 修改单元格的值
sheet['A1'] = 'New Value'

# 保存修改后的Excel文件
wb.save('example.xlsx')

# 关闭Excel文件
wb.close()

