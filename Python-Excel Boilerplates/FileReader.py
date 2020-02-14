# Filepath variable will contain path to file
filepath = ''
# Separator will here be space, change it to comma(,) in case of csv
separator = ' '
# Mapping variable will contain all mappings
mapping = {}
with open(filepath, 'w', newline='') as file:
    for line in file:
        id_, name = line.split(separator)
        mapping[id_] = name
# Mapping variable has all data, do whatever you seek.
print(mapping)
# BYE
