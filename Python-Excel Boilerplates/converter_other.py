import xlrd
import csv
import os

originalpaths = "./Excels/Contracts 2 yrs/EKKO.XLSX"

filepath = originalpaths

wb = xlrd.open_workbook(filepath)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

fields = []
rows = []

# Adding fields
for i in range(sheet.ncols):
    fields.append(sheet.cell_value(0,i))

# Adding rows
for i in range(1, sheet.nrows):
    rows.append(sheet.row_values(i))

for i in fields:
    print(i, end='\t')
print()
for i in rows[0]:
    print(i, end='\t')
