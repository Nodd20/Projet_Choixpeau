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

for list_characters in caracteristiques_persos:
    for persos_2 in caracteristiques_persos_tout:
        if list_characters['Name'] == persos_2['Name']:
            list_characters.update(persos_2)
            list_characters.update(list_characters)

print(list_characters)

def k_ppv_algo(profile, profile_data, k=5):
    '''
    '''
    distance_tab = []
    for i in range(len(profile_data)):
        for compared in profile_data:
            distance = ((int(compared['Courage']) - profile['Courage']) ** 2 + (int(compared['Ambition']) - profile['Ambition']) ** 2 + (int(compared['Intelligence']) - profile['Intelligence']) ** 2 + (int(compared['Good']) - profile['Good']) ** 2) ** 1/2
            distance_tab.append({compared['Name'], distance})
            #print(distance)

    for j in range(k):
        #print(distance_tab[k])
        pass


aimed_profile = {'Courage': 9, 'Ambition': 2, 'Intelligence': 8, 'Good': 9}

k_ppv_algo(aimed_profile, caracteristiques_persos, 5)