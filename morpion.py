# Debut

# On admet une fonction input() qui enregistre l'entree d'un joueur sous forme de str

# On admet une fonction split() qui prend en parametre une chaine de caracteres et renvoie 

# definir une fonction display(tab) qui prend en parametre un tableau tab contenant des tableaux et l'affiche ligne par ligne
def display(tab):
    # pour i dans tab
    for i in tab:
        # alors pour u dans i
        for u in i:
            #alors afficher chaque u sur la meme ligne
            print(u,end="")
        # passer a la ligne suivante
        print()

"""EVALUTAION ENTREE"""
# assigner a la variable ans le retour de la fonction split appliquee sur le retour de la fonction input
ans = input("position ?").split()
# assigner a la variable ansValid la valeur True
# si ans contient exactement deux éléments
    # alors
    # si la valeur a l'index 0 de ans est egale a "top" ou "t"
        # alors assigner a la variable a l'index 1 de ans la valeur 0
    # sinon si la valeur a l'index 0 de ans est egale a "mid" ou "middle" ou "m"
        # alors
    # sinon si la valeur a l'index 0 de ans est egale a "bot" ou "bottom" ou "b"
        #alors
# sinon
    # alors assigner a la variable ansValid la valeur False
# si ansValid est egale a False
    # alors afficher "Réponse Invalide !"
# sinon 
    #alors
"""CHANGEMENT PARTIE DE TABLEAU (USER)"""
    #


# definir une fonction morpion() qui ne prend aucun parametre
    # assigner a la variable morp le tableau [["_","_","_"],["_","_","_"],["_","_","_"]]


# Fin

display([["_ ","_ ","_ "],["_ ","_ ","_ "],["_ ","_ ","_ "]])