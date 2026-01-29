# Voici notre premier project
# nous voulons un code python qui permet a l'utilisateur de deviner un nombre:
# Entrer un nombre, et quand l'utilisateur entre le nombre, ça dit si le nombre entré est grand ou petit. ou il a trouver le bon nombre


import random

# Générer un nombre aléatoire entre 1 et 100
nombre_secret = random.randint(1, 100)

print("Devinez le nombre (entre 1 et 100) :")

while True:
    # Demander à l'utilisateur d'entrer un nombre
    essai = int(input("Entrez votre nombre : "))

    # Comparer avec le nombre secret
    if essai < nombre_secret:
        print("Trop petit ! Essayez encore.")
    elif essai > nombre_secret:
        print("Trop grand ! Essayez encore.")
    else:
        print("Bravo ! Vous avez trouvé le bon nombre :", nombre_secret)
        break
