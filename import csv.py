import csv

with open("", mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    table_naissances = [{key : value for key, value in element.items()} for element in reader]

with open("", mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    table_naissances_2020 = [{key : value for key, value in element.items()} for element in reader]

print(table_naissances_2020)