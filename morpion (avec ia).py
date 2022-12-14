# Importation pour les choix de l'ordinateur
import random
import webbrowser

# Fonction d'affichage du tableau de jeu
def display(tab):
    for i in tab:
        for u in i:
            print(u,end="")
        print()

# Fonction d'intelligence artificielle

def aiProcess(tab,playerStart):
    # l'ordi cherche des opportunités de gagner/bloquer le joueur
    # dans les diagonales
    for i in ["O  ","X  "]:
        if (tab[0][0] == i and tab[1][1] == i and tab[2][2]=="_  "):
            return [2,2]
        elif (tab[2][2] == i and tab[1][1] == i and tab[0][0]=="_  "):
            return [0,0]
        elif (tab[2][0] == i and tab[1][1] == i and tab[0][2]=="_  "):
            return [0,2]
        elif (tab[0][2] == i and tab[1][1] == i and tab[2][0]=="_  "):
            return [2,0]
        elif (((tab[2][2] == i and tab[0][0] == i and tab[1][1] == "_  ") or (tab[0][2] == i and tab[2][0] == i)) and tab[1][1] == "_  ") :
            return [1,1]
    # dans les verticales et horizontales
    for w in ["O  ","X  "]:
        for line in range(len(tab)):
            for col in range(len(tab[line])):
                if tab[line][col] == "_  ":
                    if (tab[line-1][col] == w and tab[line-2][col] == w) or (tab[line][col-1] == w and tab[line][col-2] == w):
                        return [line,col]    

    # si l'ordinateur joue en premier
    if playerStart =="n":
        if tab[0][0] == "_  ":
            return [0,0]
        elif tab[1][1] == "X  ":
            if tab[2][2] =="_  ":
                return [2,2]
            elif tab[2][2] == "O  " and tab[2][0] =="X  " and tab[0][2]=="_  " and tab[0][1]=="_  ":
                return [0,2]
            elif tab[2][2] == "O  " and tab[0][2] =="X  " and tab[2][0]=="_  " and tab[1][0]=="_  ":
                return [2,0]
        elif tab[1][1] == "_  ":
            if (tab[0][2] == "O  " or tab[2][0] == "O  ") and tab[0][2] != "X  " and tab[2][0] != "X  " and tab[2][2] != "X  ":
                return [1,1]
            elif (tab[0][2] == "O  " and tab[0][1] != "X  ") or (tab[2][0] == "O  " and tab[1][0] != "X  ") and tab[2][2] == "_  ":
                return [2,2]
            elif tab[0][2]=="_  " and tab[0][1]=="_  ":
                return [0,2]
            elif tab[2][0]=="_  " and tab[1][0]=="_  ":
                return [2,0]

    # si l'ordinateur joue en deuxième
    else: 
        if tab[1][1]=="_  ":
            return [1,1]
        elif tab[1][1] == "X  " and tab[2][2] == "_  ":
            return [2,2]
        # si cette condition passe, il est garantit que l'utilisateur ait au moins joué deux foix
        elif tab[1][1] == "O  ":
            if (tab[1][0] == "X  " and tab[1][2] == "X  "):
                if tab[0][1] == "_  " and (tab[0][0]=="_  " or tab[0][0]=="O  ") and tab[0][2]=="_  ":
                    if tab[0][0]=="_  ":
                        return [0,0]
                    elif tab[0][2]=="_  ":
                        return [0,2]
                elif tab[2][1] == "_  " and (tab[2][0]=="_  " or tab[2][0]=="O  ") and tab[2][2]=="_  ":
                    if tab[2][0]=="_  ":
                        return [2,0]
                    elif tab[2][2]=="_  ":
                        return [2,2]
            elif (tab[0][1] == "X  " and tab[2][1] == "X  "):
                if tab[1][0] == "_  " and (tab[0][0]=="_  " or tab[0][0]=="O  ") and tab[2][0]=="_  ":
                    if tab[0][0]=="_  ":
                        return [0,0]
                    elif tab[2][0]=="_  ":
                        return [2,0]
                elif tab[1][2] == "_  " and (tab[0][2]=="_  " or tab[0][2]=="O  ") and tab[2][2]=="_  ":
                    if tab[0][2]=="_  ":
                        return [0,2]
                    elif tab[2][2]=="_  ":
                        return [2,2]

    # quand on a épuisé les techniques logiques
    # on a pas vraiment de stratégie à part bloquer quand l'adversaire joue au centre et bloquer se fait automatiquement au début de la fonction
    while 1:
        # l'ordi va alors chercher une place au hasard jusqu'à en trouver une vide
        comAns = [random.randint(0,2),random.randint(0,2)]
        if tab[comAns[0]][comAns[1]] == "_  ":
            return comAns

# définition de la fonction qui va vérifier si un coup fait gagner un des joueurs
def anyWin(board, plr):
    for i in range(len(board)):
        if board[i][0] == plr and board[i][1] == plr and board[i][2] == plr or board[0][i] == plr and board[1][i] == plr and board[2][i] == plr:
            return True
    if (board[0][0] == plr and board[1][1] == plr and board[2][2] == plr) or (board[2][0] == plr and board[1][1] == plr and board[0][2] == plr):
        return True


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
        elif userStart == "tuto":
            webbrowser.open("https://fr.wikihow.com/gagner-au-morpion")
        elif userStart == "One Piece":
            print("⣿⣿⣿⣿⡿⠛⠛⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠛⠛⢿⣿⣿⣿⣿\n⣿⣿⣿⣿⠁⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠛⠛⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠈⣿⣿⣿⣿\n⣿⠋⠉⠁⠀⠀⠀⠀⢴⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠈⠉⠻⣿\n⣿⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⠟⠁⣰⡆⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⡈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⣿\n⣿⣦⣄⣀⣤⣶⣄⠀⠀⠀⠀⠙⢿⡿⠃⠀⡾⠃⣰⠟⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⢿⡄⠈⢿⡀⠈⢿⡿⠋⠀⠀⠀⠀⣠⣶⣄⣀⣀⣴⣿\n⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⢀⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾⣷⣶⣾⣿⡄⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣼⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⣀⣴⣶⣶⣄⠀⠀⠀⠀⠀⠀⣠⣴⣶⣦⣄⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⢰⣿⣿⣿⣿⣿⣷⡄⠀⠀⢀⣾⣿⣿⣿⣿⣿⣇⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⢸⣿⣿⣿⣿⣿⣿⠇⠀⠀⠘⣿⣿⣿⣿⣿⣿⡿⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⠀⠻⠿⣿⣿⠿⠋⠀⠀⠀⠀⠘⠿⢿⣿⡿⠿⠃⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⠀⠀⠀⠀⠀⠐⢿⣿⠇⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡿⠛⠲⠦⣤⣤⣤⣀⣀⣤⣤⣤⠴⠖⠛⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⢸⢧⣀⠀⢰⡇⠀⠈⠉⡏⠉⠀⢸⠀⠀⢀⣼⡇⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⣟⠀⠈⠉⣾⠳⠶⠤⣤⣧⠤⠴⢾⡗⠉⠉⠀⢇⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⡿⠋⠉⠙⠻⠛⠁⠀⠀⠀⢀⡏⠑⢶⣤⡟⠀⠀⠀⠀⡇⠀⠀⠀⣷⣠⡴⠖⢻⠀⠀⠀⠀⠈⠻⠟⠋⠉⠙⢿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣷⠀⠀⠀⠈⠉⠛⠛⠛⠛⠛⠛⠋⠉⠀⠀⠀⣾⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣧⣀⣀⠀⠀⠀⠀⠐⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⠀⠀⠀⠀⢀⣀⣠⣾⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⣿⣿⣿⣿⣇⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣤⣤⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣤⣴⣿⣿⣿⣿⣿⣿⣿")
        else:
            print("Réponse invalide!")
    # Boucle qui va répéter chaque round, prend fin quand quelqu'un gagne ou qu'il y a égalité
    while comWin == False and playerWin == False and numPlays < 9:
        # l'ordi joue ici quand le joueur joue en deuxième
        if userStart == "n":
            print("Tour de l'ordi")
            t=aiProcess(morp,"n")
            morp[t[0]][t[1]]="O  " 
            display(morp)
            numPlays +=1
        
        # on vérifie si le dernier coup de l'ordi le fait gagner
        if anyWin(morp, "O  ") ==True:
            comWin = anyWin(morp, "O  ")


        # Tour du joueur
        if comWin == False and playerWin == False and numPlays < 9 :
            print("Votre tour")
            userTurnDone = False
            nbError = 0
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
                        nbError += 1
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
                            nbError += 1

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
                                nbError += 1
                else:
                    # redemande au joueur une réponse si sa précédente n'était pas valide 
                    ansValid=False
                    nbError += 1
                if ansValid == False and nbError == 4:
                    print("olala allez c'est bon t'as gagné, \nmême pas capable d'entrer une réponse valide, \nj'en peux plus !")
                    playerWin = True
                    userTurnDone = True
                elif ansValid == False:
                    print("Réponse invalide!")
                    
        # on vérifie si le dernier coup du joueur le fait gagner
        if anyWin(morp, "X  ") ==True:
            comWin = anyWin(morp, "X  ")
        
        # l'ordi joue ici quand le joueur joue en premier
        if userStart == "y" and comWin == False and playerWin == False and numPlays < 9:
            print("Tour de l'ordi")
            t=aiProcess(morp,"y")
            morp[t[0]][t[1]]="O  " 
            display(morp)
            numPlays +=1

        # on vérifie si le dernier coup de l'ordi le fait gagner
        if anyWin(morp, "O  ") ==True:
            comWin = anyWin(morp, "O  ")

    # On affiche un message en fin de partie, pour 3 scénarios différents
    # le joueur gagner
    if playerWin == True:
        return print("Vous avez gagné!\n░██████╗░░██████╗░\n██╔════╝░██╔════╝░\n██║░░██╗░██║░░██╗░\n██║░░╚██╗██║░░╚██╗\n╚██████╔╝╚██████╔╝\n░╚═════╝░░╚═════╝░")
    # l'ordi gagne
    elif comWin == True:
        return print("Vous avez perdu!")
    # personne ne gagne
    else:
        return print("Egalité !")

morpion()