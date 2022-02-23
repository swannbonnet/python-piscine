from math import *

# 1. Créer une fonction qui demande à l'utilisateur son nom et prénom et affiche un message dans la console.

def infoUser():
    try:
        nom = input('Entre ton nom ?')
        prenom = input('Entre ton prenom ?')
        print(nom, prenom)
    except ValueError:
        print('Erreur')

#2. Créer une fonction qui demande à l'utilisateur son age et affiche l'année ou il aura 100 ans.
def infoAge():
    age = input('Quel est ton age ? ')
    year = (100 - int(age)) + 2022
    print('Tu auras 100 ans en ' , year)

#3. Écrire un programme qui, à partir de la saisie d'un rayon et d'une hauteur, calcule le volume d'un cône droit.

def volumeCone():
    rayon = input()
    hauteur = input()
    volume = pi * float(rayon)**2 * float(hauteur) /3
    print(volume)


#4. Ecrire un programme qui demande à l'utilisateur un nombre et détermine si ce nombre est pair ou impar avec un message d'affichage.

def pair_impair():
    nombre = input('Entre ton nombre : ')
    if float(nombre)%2 == 0:
        print('Chiffre pair')
    else:
        print('chiffre impair')


#5. Ecrire une fonction qui calcul la suite de fibonnaci pour un rang donnée.

def suiteFibo():
    rang = input('Entre ton rang : ')
    cpt=1;
    nombre = 0;
    while(cpt < int(rang)):
        print(nombre)
        nombre = nombre + nombre
        cpt = cpt +1


#6. Ecrire une fonction qui détermine tous les ppcm et pgcd d'un nombre donnée.


def pgcdEtPpcm():
    nombre1 = input('Entrer un nombre : ')
    nombre2 = input('Entrer un nombre : ')


#7. Ecrire une fonction qui prend deux liste en paramètres et renvoie tous les elements communs au deux listes

def elementsCommuns(liste1, liste2):
    listeCommuns = []
    for element in liste1:
        for item in liste2:
            if element == item:
                listeCommuns.append(element)
    listeCommuns = set(listeCommuns)
    print(listeCommuns)


#8. Ecrire une fonction qui determine si une chaine de caractère est un palyndrome
def palyndrome():
    chaine = input()
    if str(chaine) == str(chaine)[::-1] :
        print(chaine, " est un palindrome")
    else:
        print(chaine, " n' est pas un palindrome")