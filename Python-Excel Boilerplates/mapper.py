from texttable import Texttable
import xlrd
import csv

t = Texttable()

filepath_1 = 'Salon Wise Service Price.xlsx'
filepath_2 = 'salon_code_mapping.xlsx'
csvfilepath = 'mapped_appointment.csv'

wb_1 = xlrd.open_workbook(filepath_1)
sheet_1 = wb_1.sheet_by_index(0)
sheet_1.cell_value(0, 0)

master_fields = []
master_rows = []

# Adding fields
for i in range(sheet_1.ncols):
    master_fields.append(sheet_1.cell_value(0,i))

# Adding rows
for i in range(1, sheet_1.nrows):
    master_rows.append(sheet_1.row_values(i))

wb_2 = xlrd.open_workbook(filepath_2)
sheet_2 = wb_2.sheet_by_index(0)
sheet_2.cell_value(0, 0)

map_fields = []
map_rows = []
salon_code_map = {}

# Adding mapping fields
for i in range(sheet_2.ncols):
    map_fields.append(sheet_2.cell_value(0,i))

# Adding mapping rows
for i in range(1, sheet_2.nrows):
    map_rows.append(sheet_2.row_values(i))
    x = sheet_2.row_values(i)
    salon_code_map[x[1]] = str(x[0]).replace('.0','')

print(salon_code_map)
print('\n', len(salon_code_map.keys()))

salon_names = master_fields[0]
print(len(salon_names))

new_fields = master_fields
new_rows = []

new_fields.append("center_code")

# for i in master_rows:
#     print(i[:12])
#     break

print('Creating Data')
count = 0
for j in range(len(master_rows)):
    row = []
    row = master_rows
    x = master_rows[j][0]
    # print(master_rows[j])
    # print(count, x, end=' ')
    # print(salon_code_map[x])
    row.append(salon_code_map[x])
    new_rows.append(row)
    count += 1

print('Writing Data with ',len(new_rows))

t.add_rows(new_fields)
t.add_rows(new_rows)
print(t.draw())

# with open(csvfilepath, 'w', newline='') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(new_fields)
#     csvwriter.writerows(new_rows)
#
# print('Done')
