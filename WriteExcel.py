import openpyxl

# ����һ���µĹ�����
wb = openpyxl.Workbook()

# ����һ��������
sheet = wb.active

# д�뵥Ԫ���ֵ
sheet['A1'] = 'Hello'
sheet['B1'] = 'World'

# ���湤����
wb.save('example.xlsx')

# �رչ�����
wb.close()

