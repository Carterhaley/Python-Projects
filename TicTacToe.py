# Name: J. Carter Haley, 4 December 2016
# ticTacToe.py

#Problem: This program creates a game of tic tac toe to be played by two
#users in the shell of Python.

#Certification of Authority:
    #I certify that this lab is my work.
    
def ticTacToe():
    #This function creates a list of board positions, and a list with
    #all the possible winning combinations of those places 
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    winner = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                    (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    def draw():
        #This function prints a board in the shell by indexing the
        #list of position numbers and using various ASCII characters
        #to make it look organized
        print(board[0], "|", board[1], "|",board[2])
        print("-----------")
        print(board[3],"|", board[4],"|", board[5])
        print("-----------")
        print(board[6], "|",board[7], "|",board[8])
        print()

    def player1Turn():
        #The following line checks that the players selection is valid
        choseX = boardSelection()
        #The following if statement places the X on the board,
        #unless the position is filled already
        if board[choseX] == "X" or board[choseX] == "O":
            print("\nPosition is filled, choose another.")
            player1Turn()
        else:
            board[choseX] = "X"

    def player2Turn():
        #The following line checks that the players selection is valid
       choseO = boardSelection()
        #The following if statement places the X on the board,
        #unless the position is filled already
       if board[choseO] == "X" or board[choseO] == "O":
            print("\nPosition is filled, choose another.")
            player2Turn()
        else:
            board[choseO] = "O"

    def boardSelection():
        #This function checks the board to make sure that the user's
        #entry is valid using try and except
        while True:
            choice = input()
            try:
                choice  = int(choice)
                if choice in range(1, 10):
                    return choice
                else:
                    print("Invalid position, choose another.")
                    continue
            except ValueError:
               print("\nThat's not a number. Try again")
               continue

    def boardFill():
        #This function allows the user's to go back and forth until the board is filled
        #or until there is a winner
        count = 0
        #This loop checks to see if player 1 is a winner before each turn
        for choice in winner:
            if board[choice[0]] == board[choice[1]] == board[choice[2]] == "X":
                print("Player 1 Wins!\n")
                print("Congratulations!\n")
                return True

            #This statement checks to see if player 2 is a winner before each turn.
            if board[choice[0]] == board[choice[1]] == board[choice[2]] == "O":
                print("Player 2 Wins!\n")
                print("Congratulations!\n")
                return True
        #This loop checks if the board is full and its a tie game
        for choice in range(9):
            if board[choice] == "X" or board[choice] == "O":
                count += 1
            if count == 9:
                print("Tie game.")
                return True
    champion = False
    #This loop accepts the user's input and places it on the board, if valid
    while champion == False:
        draw()
        end = boardFill()
        if end == True:
            break
        print("Player 1, Enter a number on the board to place an X.")
        player1Turn()
        print()
        draw()
        end = boardFill()

        #This loop accepts the user's input and places it on the board, if valid
        if end == True:
            break
        print("Player 2, Enter a number on the board to place an O.")
        player2Turn()
        print()

    #After each game concludes, this statement allows the user to choose
    #whether or not they would like to play again.
    if input("Want to play again? Enter (y) for yes, or (n) if no") == "y":
        print()
        ticTacToe()
    else:
        print("\nTh
ticTacToe()
