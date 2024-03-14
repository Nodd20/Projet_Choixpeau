# coding: utf-8
'''
Codé par : Nolan DOUET, Justin LESTRAT, MOHAMED SOW

Projet NSI 3, partie II "Le Choixpeau magique"

Le programme permet !!!

Licence : CC-BY-NC-SA

github : https://github.com/Nodd20/Projet_Choixpeau 
'''

from csv import *

def importeur(fichier):
    '''
    '''
    assert fichier == str

    with open(fichier, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        element = [{key : value for key, value in element.items()} for element in reader]

    return element
    

def questionnaire(question_num, table_question):
    '''
    '''
    assert question_num == int
    assert table_question == list

    question = table_question[question_num]['Question']

    return question

def caracteriseur(dico_cara, reponse, question_num, table_question):
    '''
    '''
    assert reponse == int 
    assert dico_cara == dict

    categorie = table_question[question_num]['Categorie']
    dico_cara[categorie] = dico_cara[categorie] + reponse

    return dico_cara

def voisins(dico_voisin, dico_cara):
    '''
    '''
    distance_tab = []
    for compared in dico_voisin:
        distance = (float(compared['Courage']) - float(dico_cara['Courage']) ** 2 + float(compared['Ambition']) - float(dico_cara['Ambition']) ** 2 + float(compared['Intelligence']) - float(dico_cara['Intelligence']) ** 2 + float(compared['Good']) - float(dico_cara['Good']) ** 2) ** 0.5
        distance_tab.append({'Name': compared['Name'], 'Distance': distance, 'House': compared['House']})

    return distance_tab

def choixpeau(distance_tab, k=5):
    '''
    '''

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