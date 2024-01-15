import csv

with open("Caracteristiques_des_persos.csv", mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    caracteristiques_persos = [{key : value for key, value in element.items()} for element in reader]

with open("Characters.csv", mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    caracteristiques_persos_tout = [{key : value for key, value in element.items()} for element in reader]

print(caracteristiques_persos_tout)

