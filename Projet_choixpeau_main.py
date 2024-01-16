# coding: utf-8
'''
        ...
'''

import csv

with open("Caracteristiques_des_persos.csv", mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    caracteristiques_persos = [{key : value for key, value in element.items()} for element in reader]

with open("Characters.csv", mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    caracteristiques_persos_tout = [{key : value for key, value in element.items()} for element in reader]

list_characters = []

for persos_1 in caracteristiques_persos:
    for persos_2 in caracteristiques_persos_tout:
        if persos_1['Name'] == persos_2['Name']:
            persos_1.update(persos_2)
            list_characters.append(persos_1)

def k_ppv_algo(profile, profile_data, k=5):
    '''
    '''
    distance_tab = []
    for i in range(len(profile_data)):
        for compared in profile_data:
            distance = ((int(compared['Courage']) - profile['Courage']) ** 2 + (int(compared['Ambition']) - profile['Ambition']) ** 2 + (int(compared['Intelligence']) - profile['Intelligence']) ** 2 + (int(compared['Good']) - profile['Good']) ** 2) ** 1/2
            distance_tab.append({'Name': compared['Name'], 'Distance': distance, 'House': compared['House']})
            print(distance)
    
    sorted(distance_tab, key=lambda x: x[i]['Distance'], reverse=True)

    for j in range(k):
        print(distance_tab[j])


aimed_profile = {'Courage': 9, 'Ambition': 2, 'Intelligence': 8, 'Good': 9}

k_ppv_algo(aimed_profile, list_characters, 5)