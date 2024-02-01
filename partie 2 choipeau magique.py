profil_1= [5, 5, 5, 5]
courage = 5
ambition = 5
intelligence = 5
bonté = 5
moyenne = 0
question = ["Vous trouvez un chien abandonnée ? 1-je vais lui trouver de l'aide, 2-ça ne me fait ni chaud ni froid, 3-je lui donne un peu d'eau  ?",\
            "Quel nombre est la suite logique de cette série ? 4, 6, 9, 6, 14, 6, ... 1-6 2-17  3-19",\
            "Quel est la capital de Australie ? 1-Serbie 2-Sydney 3 Canberra",\
            "Tu es au chomage, que fait tu ? 1-ce n'est pas très grave 2-je me lance dans de gros projet 3-je trouve un travail simple"]

for i in range(0, 20):
    
choix = int(input("As-tu peur du noir ? 1-Oui, j’en suis terrifié, 2-Non, ça ne me fait ni chaud ni froid, 3-Non, au contraire, je m’y sens bien ?"))

if choix == 1:
            courage -= 2
            moyenne += 1
elif choix == 2:
            courage += 1
            moyenne += 1
elif choix == 3:
            courage += 4
            moyenne += 1
            
choix_1 = int(input("1 + 1 = 2x ? 1-x = 124, 2-2x = 2, 3-x = 1"))           
if choix == 1:
            courage -= 2
            moyenne += 1
elif choix == 2:
            courage += 1
            moyenne += 1
elif choix == 3:
            courage += 4
            moyenne += 1
            
moyenne = courage // moyenne            

print(moyenne)
            
            
            
            