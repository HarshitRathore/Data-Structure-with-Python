import xlrd
import csv
import os

originalpaths = []
paths = []

for dirname, dirnames, filenames in os.walk('./Excels/Contracts 2 yrs/'):
    for filename in filenames:
        originalpaths.append(os.path.join(dirname, filename))
        newfile = str(os.path.join(dirname, filename))
        newfile = newfile.replace('Excels', 'CSVs')
        newfile = newfile.replace('XLSX', 'csv')
        newfile = newfile.replace('\\', '/')
        x = newfile.split('/')
        # paths.append(newfile)
        paths.append(x[0]+'/'+x[1]+'/'+x[len(x)-1])

for i in range(len(paths)):
    print(i)
    filepath = originalpaths[i]

    wb = xlrd.open_workbook(filepath)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)

    csvfilepath = paths[i]

    fields = []
    rows = []

    # Adding fields
    for i in range(sheet.ncols):
        master_fields.append(sheet.cell_value(0,i))

    # Adding rows
    for i in range(1, sheet.nrows):
        master_rows.append(sheet.row_values(i))

    with open(csvfilepath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)
