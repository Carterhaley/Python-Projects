#Name: J. Carter Haley, 30 November 2016


from graphics import *
import random
import time


def wordList(file):
    infile = open(file, "r")
    words = infile.readlines()
    randomList = []
    for word in words:
        randomList.append(word)
    infile.close()
    return randomList
##
def randomWord(wList):
    randomIndex = random.randint(0,(len(wList)-1))
    secretWord = wList[randomIndex]
    secretWord = str(secretWord)
    return secretWord

def hangmanImage (incorrect, win, winWidth, winHeight, hangman):
    neckPoint = winWidth//3
    if incorrect == 1:
        # Strike 1: Draw the post
        post1 = Line(Point(winWidth-150, 75), Point(winWidth - 150 , 350))
        post1.draw(win)
        hangman.append(post1)
        post2 = Line(Point(winWidth - 250, 400), Point(neckPoint, 400))
        post2.draw(win)
        hangman.append(post2)
        post3 = Line(Point(neckPoint, 100), Point(neckPoint, 50))
        post3.draw(win)
        hangman.append(post3)
    elif incorrect == 2:
        # Strike 2: Draw the head
        head = Circle(Point(neckPoint, 120), 20)
        head.draw(win)
        hangman.append(head)
    elif incorrect == 3:
        # Strike 3: Draw the torso
        torso = Line(Point(neckPoint, 140), Point(neckPoint, 280))
        torso.draw(win)
        hangman.append(torso)
    elif incorrect == 4:
        # Strike 4: Draw the left arm
        leftArm = Line(Point(neckPoint, 170), Point(neckPoint - 30, 200))
        leftArm.draw(win)
        hangman.append(leftArm)
    elif incorrect == 5:
        # Strike 5: Draw the right arm
        rightArm = Line(Point(neckPoint, 170), Point(neckPoint + 30, 200))
        rightArm.draw(win)
        hangman.append(rightArm)
    elif incorrect == 6:
        # Strike 6: Draw the left leg
        leftLeg = Line(Point(neckPoint, 280), Point(neckPoint - 25, 305))
        leftLeg.draw(win)
        hangman.append(leftLeg)
    elif incorrect == 7:
        # Strike 7: Draw the right leg
        rightLeg = Line(Point(neckPoint, 280), Point(neckPoint + 25, 305))
        rightLeg.draw(win)
        hangman.append(rightLeg)
        time.sleep(.1)
        head.setFill("purple")
        head.setOutline("purple")
        
def main():
    winWidth = 600
    winHeight = 600
    win = GraphWin("Hangman", winWidth, winHeight)
    filename = "wordlist.txt"
    wList = wordList(filename)
    secretWord = randomWord(wList)
    secretWord1 = list(secretWord)
    blanks = "_" * len(list(secretWord))
    
    playMessage = Text(Point(winWidth // 2-30, 30), "Guess a letter.")
    playMessage.setStyle("italic")
    playMessage.draw(win)

    wordBlanks = Text(Point(winWidth // 2, winHeight - 50), blanks)
    wordBlanks.draw(win)
    
    guessInstruct = Text(Point(((winWidth // 2) - 90), 50), "Type a letter:")
    guessInstruct.draw(win)
    
    guessEntry = Entry(Point(((winWidth // 2) - 35), 50), 5)
    guessEntry.draw(win)
    guessEntry.setText("")

    guessButton = Rectangle(Point(winWidth // 2 + 50,  winHeight - 25),
                            Point(winWidth // 2 + 125,  winHeight - 50))
    guessButton.setFill("grey")
    guessButton.draw(win)
    
    guess = Text(Point(winWidth // 2 + 85, winHeight - 35), "Guess")
    guess.draw(win)

    incorrect = 0
    guessedLetters = []
    hangman = []
    champion = False
    win.getMouse()
    while incorrect < 7 and champion == False and len(hangman) < 7:
        clickPt= win.getMouse()
        
        if (clickPt.getX() < (350) and clickPt.getX() > (425)) and (clickPt.getY() <  (575) and clickPt.getY() >  (550)):
            continue
        
        guessed = guessEntry.getText().lower()
        guessEntry.setText("")
        if guessed == " " or guessed == "" or len(guessed) != 1:
            playMessage.setText("Please enter a valid character.")
            
        
        elif guessed in secretWord.lower() and not(guessed in guessedLetters):
                guessedLetters.append(guessed)
                blanks = secretWord
                for letter in secretWord:
                    if (not (letter.lower() in secretWord) or not(letter.lower() in guessedLetters)) and letter != ' ':
                            blanks = blanks.replace(letter, ' __ ')
                    
                    wordBlanks.setText(blanks)
                else:
                        playMessage.setText("Correct! {0} is in the word. Try another letter.".format(guessed.upper()))
        elif guessed in guessedLetters:
                # This letter has already been guessed, so alert the player about this and wait for another guess
                playMessage.setText("You've already guessed {0}. Try another letter.".format(guessed.upper()))
        elif len(guessedLetters) < 7:
                # Wrong guess! Add a strike and draw a new piece of the Hangman picture
                guessedLetters.append(guessed)
                incorrect += 1
                playMessage.setText('{0} is incorrect! Try again.'.format(guessed.upper()))
                hangmanImage(incorrect, win, winWidth, winHeight, hangman)
        elif blanks == secretWord:
                    champion = True

##        playMessage.move(0, -10)  # Move the message area down a bit to fill up some space

        # Update the grid to display the full, actual word that the program chose
 

        if champion == True:
            playMessage.setText("Congrats! You've guessed the word correctly.")
            playMessage.setTextColor()
            wordBlanks.setTextColor()
            wordBlanks.setText(secretWord.upper())
            wordBlanks.setStyle('italic')
            wordBlanks.setSize(15)
            guessInstruct.undraw()
            guessButton.undraw()
            guessEntry.undraw()
            guessButton.undraw()
            guess.undraw()

        elif champion == False and incorrect >= 7:
            playMessage.setText("Sorry! You didn't completely guess the word.")
            guessInstruct.undraw()
            guessButton.undraw()
            guessEntry.undraw()
            guessButton.undraw()
            guess.undraw()

                
            quitButton = guessButton
            quitButton.setFill("grey")
            quitButton.draw(win)
            quitButton = Text(Point(50, 255), 'Quit')
            win.getMouse()
        elif clickPt.getX() > winWidth // 2 + 50 or clickPt.getX() < winWidth / 2 + 150 or clickPt.getY() <  winHeight - 25 or clickPt.getY() >  winHeight - 50:
            win.close()

main()

        
##
##def correctWord(word):
##    chList = list(word)
##    guessedWord = list(guessedWord)
##    rightWord = False
##    if rightWord == False:
##        for i in range(len(chList)):
##            correctL[i] == chList[i]
##            rightWord = True
##    elif rightWord == True and i<7:
##        print("That's the correct word, " + str(guessedWord))
##
##def guessedLetter(word):
##    
##    chList = list(word)
####    print(chList)
##    
##    lettersGuessed = []
##    correctLetters = []
##    incorrectLetters  = []
##    guessedWord = ["_"] * len(chList)
##
##    winner = False
##    i = 1
##    
##    while winner == False:wordList(file)
##        print(guessedWord)
##        guessedLetter = input("Guess a letter (lowercase): ")
##        guessedLetter = guessedLetter.lower()
##
##        if len(guessedLetter) != 1:
##            print("Enter a single letter!")
##
##        elif guessedLetter in lettersGuessed:
##            print("You have already guessed that letter.")
##        elif guessedLetter in chList:
##            for i in range(len(chList)):
##                chList[i] == guessedLetter
##                guessedWord[i] = guessedLetter
##            correctLetters = correctLetters.append(guessedLetter)
##            lettersGuessed = lettersGuessed.append(guessedLetter)
##            print("correctLetters: "+ str(correctLetters))
##            print("Correct Letter! " +str(correctLetters) )
##
##        elif guessedLetter not in chList:
##            incorrectLetters.append(guessedLetter)
##            lettersGuessed.append(guessedLetter)
##            print("Incorrect, guess again.")
##            print("Letters Guessed: "+ str(incorrectLetters))
##        elif len(correctLetters) >= len(chList):
##            winner = True
##
##        winner = correctWord(str(guessedWord))
##        if  winner == True:
##            print("That's the correct word, " + str(guessedWord))
##        i+=1
##
##def main():
##    randomList = wordList("wordlist.txt")
##    secret = randomWord(randomList)
##    guessedWord = guessedLetter(str(secret))
##    correct = correctWord(guessedWord, secret)
##    print(guessedWord)
##    
##
##main()
####
