profil_1= [5, 5, 5, 5]
profil_2= [5, 5, 5, 5]
profil_3= [5, 5, 5, 5]

choix = int(input("As-tu peur du noir ? 1-Oui, j’en suis terrifié, 2-Non, ça ne me fait ni chaud ni froid, 3-Non, au contraire, je m’y sens bien ?"))

if choix == 1:
            profil_2 = [0,5,5,5]
elif choix == 2:
            profil_2 = [5,5,5,5]
elif choix == 3:
            profil_2 = [9,5,5,5]
            
choix_1 = int(input("1 + 1 = 2x ? 1-x = 124, 2-2x = 2, 3-x = 1"))           
if choix == 1:
            profil_3 = [5,5,0,5]
elif choix == 2:
            profil_3 = [5,5,5,5]
elif choix == 3:
            profil_3 = [5,5,9,5]
profil_1.append((profil_2[0] + profil_2[0])/2)
print(profil_1)
            
            
            
            