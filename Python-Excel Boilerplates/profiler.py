from texttable import Texttable
import csv
import os

all_fields = []
t = Texttable()
data = []
files = []

for cfile in os.listdir('./csvs'):
  files.append(cfile)
  with open('./csvs/'+cfile, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    all_fields.append(fields)
    # print('File Name:',cfile)
    # print('Columns Length:',len(fields))
    # print('Columns:',fields)
    # print('_'*80)

data = [files]
for i in range(52):
  temp_list = []
  for j in range(len(files)):
      if i >= len(all_fields[j]):
          x = "---NONE---"
      else:
          x = all_fields[j][i]
      temp_list.append(x)
  data.append(temp_list)
  # if all_fields[0][i] != all_fields[2][i]:
  #   data.append([all_fields[0][i], all_fields[2][i]])
t.add_rows(data)
print(t.draw())
