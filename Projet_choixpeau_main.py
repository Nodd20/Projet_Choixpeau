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
    for compared in profile_data:
        distance = ((int(compared['Courage']) - profile['Courage']) ** 2 + (int(compared['Ambition']) - profile['Ambition']) ** 2 + (int(compared['Intelligence']) - profile['Intelligence']) ** 2 + (int(compared['Good']) - profile['Good']) ** 2) ** 1/2
        distance_tab.append({'Name': compared['Name'], 'Distance': distance, 'House': compared['House']})
    
    distance_tab.sort(key=lambda d: d['Distance'])

    gryffondor = 0
    serpentard = 0
    serdaigle = 0
    poufsouffle = 0

    for j in range(k):
        if distance_tab[j]['House'] == 'Gryffindor':
            gryffondor += 1
        elif distance_tab[j]['House'] == 'Slytherin':
            serpentard += 1
        elif distance_tab[j]['House'] == 'Ravenclaw':
            serdaigle += 1
        elif distance_tab[j]['House'] == 'Hufflepuff':
            poufsouffle += 1
        
    liste_choixpeau = [gryffondor, serdaigle, serpentard, poufsouffle]
    liste_choixpeau.sort(reverse=True)

    if liste_choixpeau[0] == gryffondor:
        choixpeau = 'GRYFFONDOR'
    elif liste_choixpeau[0] == serpentard:
        choixpeau = 'SERPENTARD'
    elif liste_choixpeau[0] == serdaigle:
        choixpeau = 'SERDAIGLE'
    elif liste_choixpeau[0] == poufsouffle:
        choixpeau = 'POUFSOUFFLE'
    
    return choixpeau


aimed_profile = {'Courage': 6, 'Ambition': 5, 'Intelligence': 8, 'Good': 5}

print(k_ppv_algo(aimed_profile, list_characters, 5))