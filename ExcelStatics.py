pip install pandas
pip install openpyxl
import pandas as pd
df = pd.read_excel('example.xlsx', sheet_name='Sheet1')
print(df)
df.fillna(0, inplace=True)
df['total'] = df['scoreMath'] + df['scoreEn'] + df['scoreCh']
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = 'result'
# 将结果写入文件
for index, row in df.iterrows():
    ws.append([row['name'], row['total']])
wb.save('result.xlsx')