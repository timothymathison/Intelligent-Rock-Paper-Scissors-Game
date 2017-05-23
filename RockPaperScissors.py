import random
import atexit

convertTable = [3, 1, 2, 3, 1, 2]

def computerChoice():
    if count == 0:
        x = random.randint(1,3)
    if count == 1:
        ajust = -1
        if winHistory[-1] == "computer":
            ajust = 0
        c = computerHistory[-1]
        h = c + ajust
        h = convert(h)
        x = h + 1
        x = convert(x)
    if count == 2:
        ajust = -1
        if winHistory[-1] == "computer":
            ajust = 0
        if (winHistory[-1] == winHistory[-2]) and (computerHistory[-1] == computerHistory[-2]):
            ajust = 1
        c = computerHistory[-1]
        h = c + ajust
        h = convert(h)
        x = h + 1
        x = convert(x)
    if count >= 3:
        ajust = -1
        if winHistory[-1] == "computer":
            ajust = 0
        if (winHistory[-1] == winHistory[-2]) and (computerHistory[-1] == computerHistory[-2]):
            ajust = 1
        c = computerHistory[-1]
        h = c + ajust
        #if (humanHistory[-1] == humanHistory[-2] and humanHistory[-3] == humanHistory[-4] and count > 3):
        #    h = humanHistory[-1] + 2
        if humanHistory[-1] == humanHistory[-2] == humanHistory[-3]:
            h = humanHistory[-1]
        comSeq, accur, doubleRepeat = pattern(humanHistory, computerHistory)
        if winHistory[-3:len(winHistory)] == ['human', 'human', 'human'] and doubleRepeat == True:
            if humanHistory[-1] == humanHistory[-2]:
                h = humanHistory[-1] - 1
            else:
                h = humanHistory[-1]
        if (accur > 1) and (comSeq[0:2] == humanHistory[-2:len(humanHistory)]):
            h = comSeq[2]
            #print("pattern")
        h = convert(h)
        x = h + 1
        x = convert(x)
    return x

def pattern(lst, lst2):
    shortList = lst[-3:len(lst)]
    shortList2 = lst2[-3:len(lst2)]
    doubleRepeat = False
    if (shortList[0] == shortList[1] or shortList[1] == shortList[2]) and shortList[2] == convert(shortList[0] - 1):
        doubleRepeat = True
    patterns = []
    for i in range(0,len(lst) - 2):
        patterns.append(lst[i:(i+3)])
    index = -1
    largest = 0
    com = 0
    for seq in patterns:
        index += 1
        accur = patterns.count(seq)
        if accur >= largest:
            largest = accur
            com = index
    com = patterns[com]
    #print(patterns)
    return com, largest, doubleRepeat   

def convert(x):
    try:
        x = convertTable[x]
    except LookupError:
        x = 1
    return x

def determineWinner(cs,us):
    if us == cs:
        win = "tie"
    elif us == "rock" and cs == "paper":
        win = "computer"
    elif us == "rock" and cs == "scissors":
        win = "human"
    elif us == "paper" and cs == "rock":
        win = "human"
    elif us == "paper" and cs == "scissors":
        win = "computer"
    elif us == "scissors" and cs == "rock":
        win = "computer"
    elif us == "scissors" and cs == "paper":
        win = "human"
    return win

def filecleanup(): 
    print(prevdata, file=datafile)
    if name != "test":
        print(name+":", file=datafile)
        print("Wins:", winHistory, file=datafile)
        print("Computer Choices:", computerHistory, file=datafile)
        print("Human Choices:", humanHistory, file=datafile)
    datafile.close()


run = False
count = 0
humanScore = 0
computerScore = 0
choices = ["rock","paper","scissors"]
winHistory = []
computerHistory = []
humanHistory = []

name = input("Please enter your name: ")
datafile = open("gameData.txt", "r")
prevdata = datafile.read()
datafile.close()
#backfile = open("gameDataBackup.txt", "w")
#print(prevdata, file=backfile)
#backfile.close()
datafile = open("gameData.txt", "w")

#atexit.register(filecleanup)

while True:
    if run == False:
        print("Welcome to Rock Paper Scissors Program:")
        x = input('''Press 1 or 2 and hit Enter:
            1 - Run the Rock Paper Scissors Program
            2 - Quit
            ''')
    if run == True:
        x = input("Enter 1 to continue, or 2 to Quit: ")
    if x == "1":
        error = True
        print("R = rock.  P = paper.  S = scissors.")
        us = input("Enter your choice: ")
        cs = computerChoice()
        if us == "R" or us == "r" or us == "Rock" or us == "rock":
            us = 1
            error = False
        if us == "P" or us == "p" or us == "Paper" or us == "paper":
            us = 2
            error = False
        if us == "S" or us == "s" or us == "Scissors" or us == "scissors":
            us = 3
            error = False

        if error == False:
            computerHistory.append(cs)
            humanHistory.append(us)
            
            count = count + 1
            cs = choices[cs - 1]
            us = choices[us - 1]
            print("You chose", us, "and the computer chose", cs, ":")
            win = determineWinner(cs,us)
            
            winHistory.append(win)
            if win == "tie":
                print("The game is a tie.")
            if win == "human":
                humanScore = humanScore + 1
                print("You win!")
            if win == "computer":
                computerScore = computerScore + 1
                print("The computer wins.")
            print("Your score is", humanScore, "of", count, ".")
            print("The computer's score is", computerScore, "of", count,".")
        if error == True:
            print("That is an invalid command!")
        
        run = True
    if x == "2":
        break
    if x != ("1" or "2"):
        print("That is an invalid command!")
        run = True


filecleanup() #print to logfile
