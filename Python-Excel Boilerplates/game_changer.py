import xlrd
import csv

filepath = 'appointment_transpose.xlsx'
csvfilepath = 'final_appointment.csv'

wb = xlrd.open_workbook(filepath)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

master_fields = []
master_rows = []

# Adding fields
for i in range(sheet.ncols):
    master_fields.append(sheet.cell_value(0,i))

# Adding rows
for i in range(1, sheet.nrows):
    master_rows.append(sheet.row_values(i))

salon_names = master_fields[11:]
print(len(salon_names))

new_fields = master_fields[:11]
new_rows = []

new_fields.insert(0, "Salon")
new_fields.append("Price")
print(new_fields)

# for i in master_rows:
#     print(i[:12])
#     break

print('Creating Data')

for i in range(len(salon_names)):
    for j in range(len(master_rows)):
        row = []
        row = master_rows[j][:11]
        row.insert(0, salon_names[i].replace('Price', ''))
        row.append(master_rows[j][i+11])
        new_rows.append(row)

print('Writing Data')

with open(csvfilepath, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(new_fields)
    csvwriter.writerows(new_rows)

print('Done')
