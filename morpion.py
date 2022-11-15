# Debut

# On admet une fonction input() qui enregistre l'entree d'un joueur sous forme de str (avec optionellement un message faisant office question)

# On admet une fonction split() qui prend en parametre une chaine de caracteres str et renvoie une liste separant le contenu de str a chaque espace

# definir une fonction display(tab) qui prend en parametre un tableau tab contenant des tableaux et l'affiche ligne par ligne
def display(tab):
    # pour i dans tab
    for i in tab:
        # alors pour u dans i
        for u in i:
            #alors afficher chaque u sur la meme ligne i
            print(u,end="")
        # retour a la ligne
        print()


"""DEBUT FONCTION MORPION"""
# definir une fonction morpion() qui ne prend aucun parametre
    # assigner a la variable morp le tableau [["_  ","_  ","_  "],["_  ","_  ","_  "],["_  ","_  ","_  "]]
    # assigner a la variable numPlays la valeur 0
    # assigner a la variable choiceStartDone la valeur False
    # tant que choiceStartDone est egale a False
        # alors
        # assigner a la variable userStart le retour de la fonction input() avec le message "Voulez-vous jouer en premier ? y/n"
        # si userStart est egale a "y" ou "yes" ou "n" ou "no"





"""EVALUTAION ENTREE JOUEUR"""
# assigner a la variable userTurnDone la valeur False
# tant que userTurnDone est egale a False
    # assigner a la variable ans le retour de la fonction split appliquee sur le retour de la fonction input
    # assigner a la variable ansValid la valeur True
    # si ans contient exactement deux éléments
"""analyse ligne"""
        # alors
        # si la valeur a l'indice 0 de ans est egale a "top" ou "t"
            # alors assigner a la variable a l'indice 0 de ans la valeur 0
        # sinon si la valeur a l'indice 0 de ans est egale a "mid" ou "middle" ou "m"
            # alors assigner a la variable a l'indice 0 de ans la valeur 1
        # sinon si la valeur a l'indice 0 de ans est egale a "bot" ou "bottom" ou "b"
            # alors assigner a la variable a l'indice 0 de ans la valeur 2
        # sinon
            # alors assigner a ansValid la valeur False
"""analyse colonne"""
        # si ansValid est egale a True
            #alors
            # si la valeur a l'indice 1 de ans est egale a "left" ou "l"
                # alors assigner a la variable a l'indice 1 de ans la valeur 0
            # sinon si la valeur a l'indice 1 de ans est egale a "center" ou "c"
                # alors assigner a la variable a l'indice 1 de ans la valeur 1
            # sinon si la valeur a l'indice 1 de ans est egale a "right" ou "r"
                # alors assigner a la variable a l'indice 1 de ans la valeur 2
            # sinon
                # alors assigner a ansValid la valeur False
"""CHANGEMENT DE PARTIE USER"""
            # si ansValid est egale a True
                #alors
                # si la valeur de la variable dans morp aux indices u dans i (où i est la valeur dans ans à l'indice 0 et u est la valeur dans ans à l'indice 1) est egale a "_  "
                    # alors assigner a la variable dans morp aux indices u dans i (où i est la valeur dans ans à l'indice 0 et u est la valeur dans ans à l'indice 1) la valeur "X  "
                    # assigner a userTurnDone la valeur True
                # sinon 
                    # alors assigner a ansValid la valeur False
    # sinon
        # alors assigner a la variable ansValid la valeur False
    # si ansValid est egale a False
        # alors afficher "Réponse Invalide !"


# Fin

display([["_  ","_  ","_  "],["_  ","_  ","_  "],["_  ","_  ","_  "]])