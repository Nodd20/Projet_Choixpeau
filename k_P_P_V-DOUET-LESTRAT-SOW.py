# coding: utf-8
'''
Codé par : Nolan DOUET, Justin LESTRAT, MOHAMED SOW

Projet NSI 3, partie I "Le Choixpeau magique"

Le programme permet grâce à l'algorithme des K plus proches voisins
de déterminer la maison de différents profils.

Licence : CC-BY-NC-SA

github : https://github.com/Nodd20/Projet_Choixpeau 
'''

import csv


def k_ppv_algo(profile, profile_data, k=5):
    '''
    Cette fonction renvoie un tuple contenant la maison défini par
    l'algorithme et un dictionnaire permettant de connaitre les plus 
    proches voisins du profil initial. Elle met en oeuvre un algorithme
    des k plus proches voisins.
    
    Entrées:
        profile : dictionnaire avec les 4 caractéristiques du profil
        profile_data : table contenant l'ensemble des profils de l'univers d'Harry Potter ainsi que leur caractéristiques
        k : entier déterminant le nombre de voisins considérés (par défaut 5)
        
    Sorties:
        choixpeau : chaîne de caractères donnant la maisosn du profil
        tab_voisins : table contenant les voisins et leurs caractéristiques
    '''
    distance_tab = []
    for compared in profile_data:
        distance = ((float(compared['Courage']) - profile['Courage']) ** 2 + (float(compared['Ambition']) - profile['Ambition']) ** 2 + (float(compared['Intelligence']) - profile['Intelligence']) ** 2 + (float(compared['Good']) - profile['Good']) ** 2) ** 1/2
        distance_tab.append({'Name': compared['Name'], 'Distance': distance, 'House': compared['House']})
    
    distance_tab.sort(key=lambda d: d['Distance'])
    
    maisons = [{'house': 'Gryffindor', 'number': 0} , {'house':'Slytherin','number': 0}, {'house':'Ravenclaw','number': 0}, {'house':'Hufflepuff', 'number': 0}]
    # liste de dictionnaires nécessaire pour permettre le tri ultérieur des données
    tab_voisins = []

    for j in range(k):
        tab_voisins.append({'Name' : distance_tab[j]['Name'],'House' : distance_tab[j]['House']})
        if distance_tab[j]['House'] == 'Gryffindor':
            maisons[0]['number'] += 1
        elif distance_tab[j]['House'] == 'Slytherin':
            maisons[1]['number'] += 1
        elif distance_tab[j]['House'] == 'Ravenclaw':
            maisons[2]['number'] += 1
        elif distance_tab[j]['House'] == 'Hufflepuff':
            maisons[3]['number'] += 1
        
    maisons.sort(key=lambda x: x['number'], reverse=True) # tri des données de la liste de dictionnaire grâce à la clé 'number' 

    if maisons[0]['number'] == maisons[1]['number']:
        if maisons[0]['house'] == distance_tab[0]['House']:
            choixpeau = maisons[0]['house']
        else:
            choixpeau = maisons[1]['house']
            
    # En cas d'égalité, est pris le voisin le plus proche faisant parti des maisons égalitaires
    else:
        choixpeau = maisons[0]['house']
    
    return choixpeau, tab_voisins


# Fusion de tables début
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
# fusion de tables fin

profile_1 = {'Courage': 9, 'Ambition': 2, 'Intelligence': 8, 'Good': 9} # profiles préselectionnés 
profile_2 = {'Courage': 6, 'Ambition': 7, 'Intelligence': 9, 'Good': 7}
profile_3 = {'Courage': 3, 'Ambition': 8, 'Intelligence': 6, 'Good': 3}
profile_4 = {'Courage': 2, 'Ambition': 3, 'Intelligence': 7, 'Good': 8}
profile_5 = {'Courage': 3, 'Ambition': 4, 'Intelligence': 8, 'Good': 8}

liste_profiles = [profile_1, profile_2, profile_3, profile_4, profile_5]

yellow = '\033[93m' 
blank = '\033[0m'
blue = '\033[94m'

# IHM :

answer = int(input("Saisissez 1 si vous voulez afficher les profils préséléctionnés. Saisissez 2 pour entrer un profil."))

while answer == 1 or answer == 2:
    if answer == 1:
        numero = 1
        for profile in liste_profiles:
            print(f"La maison du profile {numero} est {yellow + k_ppv_algo(profile, list_characters)[0] + blank}, car ses voisins sont:")
            for j in range(5):
                print(f"{blue + k_ppv_algo(profile, list_characters)[1][j]['Name'] + blank}, de la maison {yellow + k_ppv_algo(profile, list_characters)[1][j]['House'] + blank}")
            numero += 1

        answer = int(input("Saisissez 1 si vous voulez afficher les profils préséléctionnés. Saisissez 2 pour entrer un profil."))

    else:
        courage = float(input("De 1 à 9 quel est son courage ?"))
        ambition = float(input("De 1 à 9 quel est son ambition ?"))
        intelligence = float(input("De 1 à 9 quel est son intelligence ?"))
        good = float(input("De 1 à 9 quel est sa bonté ?"))

        assert courage <= 9 and courage > 0, 'Courage compris entre 0 et 9'
        assert ambition <= 9 and ambition > 0, 'Ambition compris entre 0 et 9'
        assert intelligence <= 9 and intelligence > 0, 'Intelligence compris entre 0 et 9'
        assert good <= 9 and good > 0, 'Bonté compris entre 0 et 9'

        profile_settings = {'Courage': courage, 'Ambition': ambition, 'Intelligence': intelligence, 'Good': good}

        house = k_ppv_algo(profile_settings, list_characters)[0]
        print(f"Votre personnage est de la maison: {yellow + house + blank}, ses voisins sont:")
        for i in range(5):
            print(f"{blue + k_ppv_algo(profile_settings, list_characters)[1][i]['Name'] + blank}, de la maison {yellow + k_ppv_algo(profile_settings, list_characters)[1][i]['House'] + blank}")

        answer = int(input("Saisissez 1 si vous voulez afficher les profils préselectionnés. Saisissez 2 pour entrer un profil."))