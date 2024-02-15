# coding: utf-8
'''
Codé par : Nolan DOUET, Justin LESTRAT, MOHAMED SOW

Projet NSI 3, partie I "Le Choixpeau magique"

Le programme permet grâce à l'algorithme des K plus proches voisins
de déterminer la maison de différents profils.

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
    