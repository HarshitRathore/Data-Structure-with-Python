import xlrd
import csv
import os

path = './Approvers Matrix.xlsx'
csv_path= './Approvers_Matrix_2.csv'

wb = xlrd.open_workbook(path)

sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
fields = ['Category', 'Sub_Category', 'Designation', 'Approver']
rows_init = []
rows_final = []
add_details = []
print('Started Gathering Data')
for i in range(1, sheet.nrows):
    x = sheet.row_values(i)
    rows_init.append(x)
print(rows_init)
iterations = len(rows_init)
for i in range(0, iterations):
        rows_final.append([rows_init[i][0], rows_init[i][1], 'CFM', rows_init[i][2]])
        rows_final.append([rows_init[i][0], rows_init[i][1], 'CFE', rows_init[i][3]])
        rows_final.append([rows_init[i][0], rows_init[i][1], 'BFM', rows_init[i][4]])
        rows_final.append([rows_init[i][0], rows_init[i][1], 'NME', rows_init[i][5]])
print('Data Gathered')
with open(csv_path, 'w', newline='') as csvfile:
    print('File Opened')
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows_final)
    print('Data Written In File')
print('Done')
