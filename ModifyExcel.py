import openpyxl

# ��Excel�ļ�
wb = openpyxl.load_workbook('example.xlsx')

# ѡ������
sheet = wb['Sheet1']

# �޸ĵ�Ԫ���ֵ
sheet['A1'] = 'New Value'

# �����޸ĺ��Excel�ļ�
wb.save('example.xlsx')

# �ر�Excel�ļ�
wb.close()

