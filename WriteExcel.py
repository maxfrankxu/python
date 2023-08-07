import openpyxl

# 创建一个新的工作簿
wb = openpyxl.Workbook()

# 创建一个工作表
sheet = wb.active

# 写入单元格的值
sheet['A1'] = 'Hello'
sheet['B1'] = 'World'

# 保存工作簿
wb.save('example.xlsx')

# 关闭工作簿
wb.close()

