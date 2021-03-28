import csv

path = "supply.csv"
contents = csv.reader(open(path, 'r'))
print(contents)
content = [value for value in contents]
for i in content[0:5]:
    print(i)
