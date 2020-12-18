import csv

with open('name.csv', 'r') as file:
    result = csv.reader(file)
    for row in result:
        print(row)
