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
    
    distance_tab.sort(key=lambda d: d['Distance'])

    return distance_tab

