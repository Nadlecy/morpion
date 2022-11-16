# Debut

# On admet une fonction random() qui retourne un integer aléatoire entre 0 et 2 inclus
import random
# On admet une fonction input() qui enregistre l'entree d'un joueur sous forme de str (avec optionellement un message faisant office question)
# On admet une fonction split() qui prend en parametre une chaine de caracteres str et renvoie une liste separant le contenu de str a chaque espace
# On admet une fonction len() qui renvoie la longueur d'une liste en parametre

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


# definir une fonction morpion() qui ne prend aucun parametre
def morpion():
    # assigner a la variable morp le tableau [["_  ","_  ","_  "],["_  ","_  ","_  "],["_  ","_  ","_  "]]
    morp = [["_  ","_  ","_  "],["_  ","_  ","_  "],["_  ","_  ","_  "]]
    # assigner a la variable numPlays la valeur 0
    numPlays = 0
    # assigner a la variable playerWin la valeur False
    playerWin = False
    # assigner a la variable comWin la valeur False
    comWin = False
    # assigner a la variable choiceStartDone la valeur False
    choiceStartDone = False
    # tant que choiceStartDone est egale a False
    while choiceStartDone == False :
        # alors
        # assigner a la variable userStart le retour de la fonction input() avec le message "Voulez-vous jouer en premier ? y/n"
        userStart = input("Voulez-vous jouer en premier ? y/n\n")
        # si userStart est egale a "y" ou "n"
        if userStart == "y" or userStart == "n":
            # alors assigner a choiceStartDone la valeur True
            choiceStartDone = True
        # sinon
        else:
            # alors afficher le message "Réponse invalide!"
            print("Réponse invalide!")
    # tant que comWin est egale a False et playerWin est egale a False et numPlays est inferieure a 9
    while comWin == False and playerWin == False and numPlays < 9:
        # alors
        # si userStart est egale a "n":
        if userStart == "n":
            # alors assigner a la variable comTurnDone la valeur False
            comTurnDone = False
            # afficher le message "Tour de l'ordi"
            print("Tour de l'ordi")
            # tant que comTurnDone est egale a False
            while comTurnDone == False:
                # alors
                # assigner a comAns un tableau contenant deux retours de la fonction random()
                comAns = [random.randint(0,2),random.randint(0,2)]
                # si la valeur de la variable dans morp a l'indice u dans i (où i est la valeur dans comAns à l'indice 0 et u est la valeur dans comAns à l'indice 1) est egale a "_  "
                if morp[comAns[0]][comAns[1]] == "_  ":
                    # alors assigner a la variable dans morp aux indices u dans i (où i est la valeur dans comAns à l'indice 0 et u est la valeur dans comAns à l'indice 1) la valeur "O  "
                    morp[comAns[0]][comAns[1]] = "O  "
                    # utiliser la fonction display() avec morp en parametre
                    display(morp)
                    # incrementer numPlays de 1
                    numPlays += 1
                    # assigner a comTurnDone la valeur True
                    comTurnDone = True
        
        # pour i chaque valeur jusqu'au retour de la fonction len ayant pour parametre "morp" moins 1
        for i in range(len(morp)):
            # alors
            # si les valeurs d'indice 0, 1 et 2 dans la liste d'indice i dans morp sont toutes egales a "X  " ou les valeurs d'indice i dans les listes d'indices 0, 1 et 2 dans morp sont toutes egales a "X  "
            if morp[i][0] == "X  " and morp[i][1] == "X  " and morp[i][2] == "X  ":
                # alors assigner a playerWin la valeur True
                playerWin = True
            # sinon si les valeurs d'indice 0, 1 et 2 dans la liste d'indice i dans morp sont toutes egales a "O  " ou les valeurs d'indice i dans les listes d'indices 0, 1 et 2 dans morp sont toutes egales a "O  "
            elif morp[i][0] == "O  " and morp[i][1] == "O  " and morp[i][2] == "O  ":
                # alors assigner a comWin la valeur True
                comWin = True
        # si la valeur d'indice 0 dans la liste d'indice 0 de morp, la valeur d'indice 1 dans la liste d'indice 1 dans morp et la valeur d'indice 2 de la liste d'indice 2 dans morp sont egales a "X  " ou la valeur d'indice 0 dans la liste d'indice 2 de morp, la valeur d'indice 1 dans la liste d'indice 1 dans morp et la valeur d'indice 2 de la liste d'indice 0 dans morp sont egales a "X  "
        if (morp[0][0] == "X  " and morp[1][1] == "X  " and morp[2][2] == "X  ") or (morp[2][0] == "X  " and morp[1][1] == "X  " and morp[0][2] == "X  "):
                # alors assigner a playerWin la valeur True
                playerWin = True
        # sinon si la valeur d'indice 0 dans la liste d'indice 0 de morp, la valeur d'indice 1 dans la liste d'indice 1 dans morp et la valeur d'indice 2 de la liste d'indice 2 dans morp sont egales a "O  " ou la valeur d'indice 0 dans la liste d'indice 2 de morp, la valeur d'indice 1 dans la liste d'indice 1 dans morp et la valeur d'indice 2 de la liste d'indice 0 dans morp sont egales a "O  "
        if (morp[0][0] == "O  " and morp[1][1] == "O  " and morp[2][2] == "O  ") or (morp[2][0] == "O  " and morp[1][1] == "O  " and morp[0][2] == "O  "):
                # alors assigner a comWin la valeur True
                comWin = True

        # si numPlays est inferieure a 9
        if numPlays < 9 :
            # alors afficher le message "Votre tour"
            print("Votre tour")
            # assigner a la variable userTurnDone la valeur False
            userTurnDone = False
            # tant que userTurnDone est egale a False
            while userTurnDone == False:
                # assigner a la variable ans le retour de la fonction split appliquee sur le retour de la fonction input avec le message "position ? top/middle/bottom left/center/right"
                ans = input("position ? top/middle/bottom left/center/right\n").split()
                # assigner a la variable ansValid la valeur True
                ansValid = True
                # si le retour de la fonction len() avec ans en parametre est egal a 2
                if len(ans) == 2:
                    # alors
                    # si la valeur a l'indice 0 de ans est egale a "top" ou "t"
                    if ans[0] == "top" or ans[0] == "t":
                        # alors assigner a la variable a l'indice 0 de ans la valeur 0
                        ans[0]=0
                    # sinon si la valeur a l'indice 0 de ans est egale a "mid" ou "middle" ou "m"
                    elif ans[0] == "mid" or ans[0] == "middle" or ans[0] == "m":
                        # alors assigner a la variable a l'indice 0 de ans la valeur 1
                        ans[0] = 1
                    # sinon si la valeur a l'indice 0 de ans est egale a "bot" ou "bottom" ou "b"
                    elif ans[0] == "bot" or ans[0] == "bottom" or ans[0] == "b":
                        # alors assigner a la variable a l'indice 0 de ans la valeur 2
                        ans[0] = 2
                    # sinon
                    else:
                        # alors assigner a ansValid la valeur False
                        ansValid = False
                    # si ansValid est egale a True
                    if ansValid == True:
                        #alors
                        # si la valeur a l'indice 1 de ans est egale a "left" ou "l"
                        if ans[1] == "left" or ans[1] == "l":
                            # alors assigner a la variable a l'indice 1 de ans la valeur 0
                            ans[1] = 0
                        # sinon si la valeur a l'indice 1 de ans est egale a "center" ou "c"
                        elif ans[1] == "center" or ans[1] == "c":
                            # alors assigner a la variable a l'indice 1 de ans la valeur 1
                            ans[1] = 1
                        # sinon si la valeur a l'indice 1 de ans est egale a "right" ou "r"
                        elif ans[1] == "right" or ans[1] == "r":
                            # alors assigner a la variable a l'indice 1 de ans la valeur 2
                            ans[1] = 2
                        # sinon
                        else:
                            # alors assigner a ansValid la valeur False
                            ansValid = False

                        # si ansValid est egale a True
                        if ansValid == True:
                            #alors
                            # si la valeur de la variable dans morp aux indices u dans i (où i est la valeur dans ans à l'indice 0 et u est la valeur dans ans à l'indice 1) est egale a "_  "
                            if morp[ans[0]][ans[1]] == "_  ":
                                # alors assigner a la variable dans morp aux indices u dans i (où i est la valeur dans ans à l'indice 0 et u est la valeur dans ans à l'indice 1) la valeur "X  "
                                morp[ans[0]][ans[1]] = "X  "
                                # utiliser la fonction display() avec morp en parametre
                                display(morp)
                                # incrementer numPlays de 1
                                numPlays+=1
                                # assigner a userTurnDone la valeur True
                                userTurnDone = True
                            # sinon 
                            else:
                                # alors assigner a ansValid la valeur False
                                ansValid=False
                # sinon
                else:
                    # alors assigner a la variable ansValid la valeur False
                    ansValid=False
                # si ansValid est egale a False
                if ansValid == False:
                    # alors afficher "Réponse Invalide !"
                    print("Réponse invalide!")
        
        # pour i chaque valeur jusqu'au retour de la fonction len ayant pour parametre "morp" moins 1
        for i in range(len(morp)):
            # alors
            # si les valeurs d'indice 0, 1 et 2 dans la liste d'indice i dans morp sont toutes egales a "X  " ou les valeurs d'indice i dans les listes d'indices 0, 1 et 2 dans morp sont toutes egales a "X  "
            if morp[i][0] == "X  " and morp[i][1] == "X  " and morp[i][2] == "X  ":
                # alors assigner a playerWin la valeur True
                playerWin = True
            # sinon si les valeurs d'indice 0, 1 et 2 dans la liste d'indice i dans morp sont toutes egales a "O  " ou les valeurs d'indice i dans les listes d'indices 0, 1 et 2 dans morp sont toutes egales a "O  "
            elif morp[i][0] == "O  " and morp[i][1] == "O  " and morp[i][2] == "O  ":
                # alors assigner a comWin la valeur True
                comWin = True
        # si la valeur d'indice 0 dans la liste d'indice 0 de morp, la valeur d'indice 1 dans la liste d'indice 1 dans morp et la valeur d'indice 2 de la liste d'indice 2 dans morp sont egales a "X  " ou la valeur d'indice 0 dans la liste d'indice 2 de morp, la valeur d'indice 1 dans la liste d'indice 1 dans morp et la valeur d'indice 2 de la liste d'indice 0 dans morp sont egales a "X  "
        if (morp[0][0] == "X  " and morp[1][1] == "X  " and morp[2][2] == "X  ") or (morp[2][0] == "X  " and morp[1][1] == "X  " and morp[0][2] == "X  "):
                # alors assigner a playerWin la valeur True
                playerWin = True
        # sinon si la valeur d'indice 0 dans la liste d'indice 0 de morp, la valeur d'indice 1 dans la liste d'indice 1 dans morp et la valeur d'indice 2 de la liste d'indice 2 dans morp sont egales a "O  " ou la valeur d'indice 0 dans la liste d'indice 2 de morp, la valeur d'indice 1 dans la liste d'indice 1 dans morp et la valeur d'indice 2 de la liste d'indice 0 dans morp sont egales a "O  "
        if (morp[0][0] == "O  " and morp[1][1] == "O  " and morp[2][2] == "O  ") or (morp[2][0] == "O  " and morp[1][1] == "O  " and morp[0][2] == "O  "):
                # alors assigner a comWin la valeur True
                comWin = True
        
        # si userStart est egale a "y" et numPlays est inferieure a 9:
        if userStart == "y" and numPlays < 9:
            # alors assigner a la variable comTurnDone la valeur False
            comTurnDone = False
            # afficher le message "Tour de l'ordi"
            print("Tour de l'ordi")
            # tant que comTurnDone est egale a False
            while comTurnDone == False:
                # alors
                # assigner a comAns un tableau contenant deux retours de la fonction random()
                comAns = [random.randint(0,2),random.randint(0,2)]
                # si la valeur de la variable dans morp a l'indice u dans i (où i est la valeur dans comAns à l'indice 0 et u est la valeur dans comAns à l'indice 1) est egale a "_  "
                if morp[comAns[0]][comAns[1]] == "_  ":
                    # alors assigner a la variable dans morp aux indices u dans i (où i est la valeur dans comAns à l'indice 0 et u est la valeur dans comAns à l'indice 1) la valeur "O  "
                    morp[comAns[0]][comAns[1]] = "O  "
                    # utiliser la fonction display() avec morp en parametre
                    display(morp)
                    # incrementer numPlays de 1
                    numPlays += 1
                    # assigner a comTurnDone la valeur True
                    comTurnDone = True

        # pour i chaque valeur jusqu'au retour de la fonction len ayant pour parametre "morp" moins 1
        for i in range(len(morp)):
            # alors
            # si les valeurs d'indice 0, 1 et 2 dans la liste d'indice i dans morp sont toutes egales a "X  " ou les valeurs d'indice i dans les listes d'indices 0, 1 et 2 dans morp sont toutes egales a "X  "
            if morp[i][0] == "X  " and morp[i][1] == "X  " and morp[i][2] == "X  ":
                # alors assigner a playerWin la valeur True
                playerWin = True
            # sinon si les valeurs d'indice 0, 1 et 2 dans la liste d'indice i dans morp sont toutes egales a "O  " ou les valeurs d'indice i dans les listes d'indices 0, 1 et 2 dans morp sont toutes egales a "O  "
            elif morp[i][0] == "O  " and morp[i][1] == "O  " and morp[i][2] == "O  ":
                # alors assigner a comWin la valeur True
                comWin = True
        # si la valeur d'indice 0 dans la liste d'indice 0 de morp, la valeur d'indice 1 dans la liste d'indice 1 dans morp et la valeur d'indice 2 de la liste d'indice 2 dans morp sont egales a "X  " ou la valeur d'indice 0 dans la liste d'indice 2 de morp, la valeur d'indice 1 dans la liste d'indice 1 dans morp et la valeur d'indice 2 de la liste d'indice 0 dans morp sont egales a "X  "
        if (morp[0][0] == "X  " and morp[1][1] == "X  " and morp[2][2] == "X  ") or (morp[2][0] == "X  " and morp[1][1] == "X  " and morp[0][2] == "X  "):
                # alors assigner a playerWin la valeur True
                playerWin = True
        # sinon si la valeur d'indice 0 dans la liste d'indice 0 de morp, la valeur d'indice 1 dans la liste d'indice 1 dans morp et la valeur d'indice 2 de la liste d'indice 2 dans morp sont egales a "O  " ou la valeur d'indice 0 dans la liste d'indice 2 de morp, la valeur d'indice 1 dans la liste d'indice 1 dans morp et la valeur d'indice 2 de la liste d'indice 0 dans morp sont egales a "O  "
        if (morp[0][0] == "O  " and morp[1][1] == "O  " and morp[2][2] == "O  ") or (morp[2][0] == "O  " and morp[1][1] == "O  " and morp[0][2] == "O  "):
                # alors assigner a comWin la valeur True
                comWin = True

    # Si playerWin est egale a True
    if playerWin == True:
        # alors renvoyer le message "Vous avez gagné!"
        return print("Vous avez gagné!")
    # Sinon si comWin est egale a True
    if comWin == True:
        # alors renvoyer le message "Vous avez perdu!"
        return print("Vous avez perdu!")
    # Sinon 
    else:
        # alors renvoyer le message "Egalité!"
        return print("Egalité !")

morpion()
# Fin