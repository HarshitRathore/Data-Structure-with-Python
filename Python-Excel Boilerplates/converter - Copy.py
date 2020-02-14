import xlrd
import csv
import os

path = './Final List.xlsx'
csv_path= './New List.csv'

wb = xlrd.open_workbook(path)

sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
fields = []
rows = []
print('Started Gathering Data')
for i in range(sheet.ncols):
        fields.append(sheet.cell_value(0,i))
fields.append('WBS-Series')
"""for i in range(sheet.ncols):
    for j in range(1, sheet.nrows):
        if i == 2:
            print(sheet.cell_value(j,2).replace('(', ' ('))
        else:
            print(sheet.cell_value(j,i))
"""
for i in range(1, sheet.nrows):
    x = sheet.row_values(i)
    x[2] = x[2].replace('(', ' (')
    x[3] = x[3][4:]
    x.append(x[3][0:2])
    rows.append(x)
print('Data Gathered')
with open(csv_path, 'w', newline='') as csvfile:
    print('File Opened')
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
    print('Data Written In File')
print('Done')
