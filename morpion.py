# Importation pour les choix de l'ordinateur
import random

# Fonction d'affichage du tableau de jeu
def display(tab):
    """
    Function display(tab)

    tab is a tuple or a list in 2 dimensions.

    display(tab) returns None and display in the shell a simple visual representation of tab,
    splitting each list/tuple in tab on different lines, removing the container syntax 
    (which means on the contents are visible, [["X ","Y "],["A ","B "]] would be shown as the following:
    X Y 
    A B
    )
    """
    for i in tab:
        for u in i:
            print(u,end="")
        print()


# définition de la fonction qui va contenir notre jeu
def morpion():
    # Initialisation
    morp = [["_  ","_  ","_  "],["_  ","_  ","_  "],["_  ","_  ","_  "]]
    numPlays = 0
    playerWin = False
    comWin = False
    # on va offrir au joueur s'il veut jouer en premier ou en deuxième, dans une boucle qui ne prend fin que lorsque la réponse est utilisable
    choiceStartDone = False
    while choiceStartDone == False :
        userStart = input("Voulez-vous jouer en premier ? y/n\n")
        if userStart == "y" or userStart == "n":
            choiceStartDone = True
        else:
            print("Réponse invalide!")
    # Boucle qui va répéter chaque round, prend fin quand quelqu'un gagne ou qu'il y a égalité
    while comWin == False and playerWin == False and numPlays < 9:
        # l'ordi joue ici quand le joueur joue en deuxième
        if userStart == "n":
            comTurnDone = False
            print("Tour de l'ordi")
            while comTurnDone == False:
                # l'ordi va chercher une place au hasard jusqu'à en trouver une vide
                comAns = [random.randint(0,2),random.randint(0,2)]
                if morp[comAns[0]][comAns[1]] == "_  ":
                    morp[comAns[0]][comAns[1]] = "O  "
                    display(morp)
                    numPlays += 1
                    comTurnDone = True
        
        # on vérifie si le dernier coup de l'ordi le fait gagner
        for i in range(len(morp)):
            if morp[i][0] == "O  " and morp[i][1] == "O  " and morp[i][2] == "O  " or morp[0][i] == "O  " and morp[1][i] == "O  " and morp[2][i] == "O  ":
                comWin = True
        if (morp[0][0] == "O  " and morp[1][1] == "O  " and morp[2][2] == "O  ") or (morp[2][0] == "O  " and morp[1][1] == "O  " and morp[0][2] == "O  "):
                comWin = True

        # Tour du joueur
        if comWin == False and playerWin == False and numPlays < 9 :
            print("Votre tour")
            userTurnDone = False
            # on va vérifier que le joueur joue à un endroit possible
            while userTurnDone == False:
                ans = input("position ? top/middle/bottom left/center/right\n").split()
                ansValid = True
                if len(ans) == 2:
                    # choix emplacement vertical
                    if ans[0] == "top" or ans[0] == "t":
                        ans[0]=0
                    elif ans[0] == "mid" or ans[0] == "middle" or ans[0] == "m":
                        ans[0] = 1
                    elif ans[0] == "bot" or ans[0] == "bottom" or ans[0] == "b":
                        ans[0] = 2
                    # on redemande au joueur une réponse si sa précédente n'était pas valide 
                    else:
                        ansValid = False
                    # choix emplacement horizontal
                    if ansValid == True:
                        if ans[1] == "left" or ans[1] == "l":
                            ans[1] = 0
                        elif ans[1] == "center" or ans[1] == "c":
                            ans[1] = 1
                        elif ans[1] == "right" or ans[1] == "r":
                            ans[1] = 2
                        # on redemande au joueur une réponse si sa précédente n'était pas valide 
                        else:
                            ansValid = False

                        if ansValid == True:
                            # est-ce que le joueur a choisi un emplacement vide
                            if morp[ans[0]][ans[1]] == "_  ":
                                morp[ans[0]][ans[1]] = "X  "
                                display(morp)
                                numPlays+=1
                                userTurnDone = True
                            else:
                                # on redemande au joueur une réponse si sa précédente n'était pas valide 
                                ansValid=False
                else:
                    # redemande au joueur une réponse si sa précédente n'était pas valide 
                    ansValid=False
                if ansValid == False:
                    print("Réponse invalide!")
        
        # on vérifie si le dernier coup du joueur le fait gagner
        for i in range(len(morp)):
            if morp[i][0] == "X  " and morp[i][1] == "X  " and morp[i][2] == "X  " or morp[0][i] == "X  " and morp[1][i] == "X  " and morp[2][i] == "X  ":
                playerWin = True
        if (morp[0][0] == "X  " and morp[1][1] == "X  " and morp[2][2] == "X  ") or (morp[2][0] == "X  " and morp[1][1] == "X  " and morp[0][2] == "X  "):
                playerWin = True
        
        # l'ordi joue ici quand le joueur joue en premier
        if userStart == "y" and comWin == False and playerWin == False and numPlays < 9:
            comTurnDone = False
            print("Tour de l'ordi")
            while comTurnDone == False:
                # l'ordi va chercher une place au hasard jusqu'à en trouver une vide
                comAns = [random.randint(0,2),random.randint(0,2)]
                if morp[comAns[0]][comAns[1]] == "_  ":
                    morp[comAns[0]][comAns[1]] = "O  "
                    display(morp)
                    numPlays += 1
                    comTurnDone = True

        # on vérifie si le dernier coup de l'ordi le fait gagner
        for i in range(len(morp)):
            if morp[i][0] == "O  " and morp[i][1] == "O  " and morp[i][2] == "O  " or morp[0][i] == "O  " and morp[1][i] == "O  " and morp[2][i] == "O  ":
                comWin = True
        if (morp[0][0] == "O  " and morp[1][1] == "O  " and morp[2][2] == "O  ") or (morp[2][0] == "O  " and morp[1][1] == "O  " and morp[0][2] == "O  "):
                comWin = True

    # On affiche un message en fin de partie, pour 3 scénarios différents
    # le joueur gagner
    if playerWin == True:
        return print("Vous avez gagné!")
    # l'ordi gagne
    elif comWin == True:
        return print("Vous avez perdu!")
    # personne ne gagne
    else:
        return print("Egalité !")

morpion()