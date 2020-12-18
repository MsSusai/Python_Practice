import csv

with open('name.csv', 'r') as file:
    result = csv.reader(file)
    for row in result:
        print(row)

with open('name.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['张芳', '女', '20'])
    writer.writerow(['王虎', '男', '22'])
