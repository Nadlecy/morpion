# Debut

# On admet une fonction len() qui renvoie la longueur d'une liste en parametre
# On admet une fonction random() qui retourne un integer aléatoire entre 0 et 2 inclus
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
"""INITIALISATION MOTERHFUCKKRe"""
    # assigner a la variable morp le tableau [["_  ","_  ","_  "],["_  ","_  ","_  "],["_  ","_  ","_  "]]
    # assigner a la variable numPlays la valeur 0
    # assigner a la variable playerWin la valeur False
    # assigner a la variable comWin la valeur False
    # assigner a la variable choiceStartDone la valeur False
"""JOUER EN PREMIER ?????"""
    # tant que choiceStartDone est egale a False
        # alors
        # assigner a la variable userStart le retour de la fonction input() avec le message "Voulez-vous jouer en premier ? y/n"
        # si userStart est egale a "y" ou "n"
            # alors assigner a choiceStartDone la valeur True
        # sinon
            # alors afficher le message "Réponse invalide!"
"""DEBUT BOUCLE ROUNDS"""
    # tant que comWin est egale a False et playerWin est egale a False et numPlays est inferieure a 9
        # alors
"""ENTREE ORDI SI JOUE EN PREMIERIERIMLEILMEI"""
        # si userStart est egale a "n":
            # alors assigner a la variable comTurnDone la valeur False
            # afficher le message "Tour de l'ordi"
            # tant que comTurnDone est egale a False
                # alors
                # assigner a comAns un tableau contenant deux retours de la fonction random()
                # si la valeur de la variable dans morp aux indices u dans i (où i est la valeur dans comAns à l'indice 0 et u est la valeur dans comAns à l'indice 1) est egale a "_  "
                    # alors assigner a la variable dans morp aux indices u dans i (où i est la valeur dans comAns à l'indice 0 et u est la valeur dans comAns à l'indice 1) la valeur "O  "
                    # utiliser la fonction display() avec morp en parametre
                    # incrementer numPlays de 1
                    # assigner a comTurnDone la valeur True
"""EVALUTAION ENTREE JOUEUR"""
        # si numPlays est inferieure a 9
            # alors afficher le message "Votre tour"
            # assigner a la variable userTurnDone la valeur False
            # tant que userTurnDone est egale a False
                # assigner a la variable ans le retour de la fonction split appliquee sur le retour de la fonction input avec le message "position ?"
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
                                # utiliser la fonction display() avec morp en parametre
                                # incrementer numPlays de 1
                                # assigner a userTurnDone la valeur True
                            # sinon 
                                # alors assigner a ansValid la valeur False
            # sinon
                # alors assigner a la variable ansValid la valeur False
            # si ansValid est egale a False
                # alors afficher "Réponse Invalide !"
"""ENTREE ORDI SI JOUE EN DEUXIEIIEMIEMEI"""
        # si userStart est egale a "y" et numPlays est inferieure a 9:
            # alors assigner a la variable comTurnDone la valeur False
            # afficher le message "Tour de l'ordi"
            # tant que comTurnDone est egale a False
                # alors
                # assigner a comAns un tableau contenant deux retours de la fonction random()
                # si la valeur de la variable dans morp aux indices u dans i (où i est la valeur dans comAns à l'indice 0 et u est la valeur dans comAns à l'indice 1) est egale a "_  "
                    # alors assigner a la variable dans morp aux indices u dans i (où i est la valeur dans comAns à l'indice 0 et u est la valeur dans comAns à l'indice 1) la valeur "O  "
                    # utiliser la fonction display() avec morp en parametre
                    # incrementer numPlays de 1
                    # assigner a comTurnDone la valeur True
"""LINE CHECK"""
        # pour i chaque valeur jusqu'a la longueur de morp moins 1
            # alors
            # si les valeurs d'indice 0, 1 et 2 dans la liste d'indice i dans morp sont toutes egales a "X  " ou les valeurs d'indice i dans les listes d'indices 0, 1 et 2 dans morp sont toutes egales a "X  "
                # alors assigner a playerWin la valeur True
            # sinon si les valeurs d'indice 0, 1 et 2 dans la liste d'indice i dans morp sont toutes egales a "O  " ou les valeurs d'indice i dans les listes d'indices 0, 1 et 2 dans morp sont toutes egales a "O  "
                # alors assigner a comWin la valeur True
        # si la valeur d'indice 0 dans la liste d'indice 0 de morp, la valeur d'indice 1 dans la liste d'indice 1 dans morp et la valeur d'indice 2 de la liste d'indice 2 dans morp sont egales a "X  " ou la valeur d'indice 0 dans la liste d'indice 2 de morp, la valeur d'indice 1 dans la liste d'indice 1 dans morp et la valeur d'indice 2 de la liste d'indice 0 dans morp sont egales a "X  "
                # alors assigner a playerWin la valeur True
        # sinon si la valeur d'indice 0 dans la liste d'indice 0 de morp, la valeur d'indice 1 dans la liste d'indice 1 dans morp et la valeur d'indice 2 de la liste d'indice 2 dans morp sont egales a "O  " ou la valeur d'indice 0 dans la liste d'indice 2 de morp, la valeur d'indice 1 dans la liste d'indice 1 dans morp et la valeur d'indice 2 de la liste d'indice 0 dans morp sont egales a "O  "
                # alors assigner a comWin la valeur True
"""CONCLUSION"""
    # Si playerWin est egale a True
        # alors renvoyer le message "Vous avez gagné!"
    # Sinon si comWin est egale a True
        # alors renvoyer le message "Vous avez perdu!"
    # Sinon 
        # alors renvoyer le message "Egalité!"

# Fin