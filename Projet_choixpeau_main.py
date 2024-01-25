# coding: utf-8
'''
        ...
'''

import csv


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
    tab_voisins = []

    for j in range(k):
        tab_voisins.append({distance_tab[j]['Name']: distance_tab[j]['House']})
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

    if liste_choixpeau[0] == liste_choixpeau[1]:
        if liste_choixpeau[0] == liste_choixpeau[2]:
            choixpeau = liste_choixpeau[0]
        choixpeau = k_ppv_algo(profile, profile_data, 3)
    elif liste_choixpeau[0] == gryffondor:
        choixpeau = 'GRYFFONDOR'
    elif liste_choixpeau[0] == serpentard:
        choixpeau = 'SERPENTARD'
    elif liste_choixpeau[0] == serdaigle:
        choixpeau = 'SERDAIGLE'
    elif liste_choixpeau[0] == poufsouffle:
        choixpeau = 'POUFSOUFFLE'
    
    return choixpeau, tab_voisins


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

profile_1 = {'Courage': 9, 'Ambition': 2, 'Intelligence': 8, 'Good': 9}
profile_2 = {'Courage': 6, 'Ambition': 7, 'Intelligence': 9, 'Good': 7}
profile_3 = {'Courage': 3, 'Ambition': 8, 'Intelligence': 6, 'Good': 3}
profile_4 = {'Courage': 2, 'Ambition': 3, 'Intelligence': 7, 'Good': 8}
profile_5 = {'Courage': 3, 'Ambition': 4, 'Intelligence': 8, 'Good': 8}

'''
print(f"La maison du profil 1 est {k_ppv_algo(profile_1, list_characters)[0]}, car vos voisins sont {k_ppv_algo(profile_1, list_characters)[1]}")
print(f"La maison du profil 2 est {k_ppv_algo(profile_2, list_characters)[0]}, car vos voisins sont {k_ppv_algo(profile_2, list_characters)[1]}")
print(f"La maison du profil 3 est {k_ppv_algo(profile_3, list_characters)[0]}, car vos voisins sont {k_ppv_algo(profile_3, list_characters)[1]}")
print(f"La maison du profil 4 est {k_ppv_algo(profile_4, list_characters)[0]}, car vos voisins sont {k_ppv_algo(profile_4, list_characters)[1]}")
print(f"La maison du profil 5 est {(k_ppv_algo(profile_5, list_characters))[0][0]}, car vos voisins sont {k_ppv_algo(profile_5, list_characters)[1]}")
'''

yellow = '\033[93m' 
blank = '\033[0m'
green = '\033[94m'

answer = int(input("Saisissez 1 si vous voulez afficher les profils préséléctionnés. Saisissez 2 pour entrer un profil."))

while answer == 1 or answer == 2:
    if answer == 1: 
        answer = int(input("Saisissez 1 si vous voulez afficher les profils préséléctionnés. Saisissez 2 pour entrer un profil."))

    else:
        courage = int(input("De 1 à 9 quel est son courage ?"))
        ambition = int(input("De 1 à 9 quel est son ambition ?"))
        intelligence = int(input("De 1 à 9 quel est son intelligence ?"))
        good = int(input("De 1 à 9 quel est sa bonté ?"))

        profile_settings = {'Courage': courage, 'Ambition': ambition, 'Intelligence': intelligence, 'Good': good}

        house = k_ppv_algo(profile_settings, list_characters)[0]
        print(f"Votre personnage est de la maison:{yellow + house + blank}, ses voisins sont{k_ppv_algo(profile_settings, list_characters)[1]}")
        answer = int(input("Saisissez 1 si vous voulez afficher les profils préséléctionnés. Saisissez 2 pour entrer un profil."))