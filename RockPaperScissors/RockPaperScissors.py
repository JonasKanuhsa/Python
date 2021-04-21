'''
To make a fully functional game of Rock, Paper, Scissors!
@author: JonasKanuhsa
'''

import random

keepPlaying = True

#Loop:Make a game loop that continues while keepPlaying is true.
    #Print out a statement to welcome user to the game
while(keepPlaying):
    print("Welcome to Rock Paper Scissors!")
    print("Best two out of three. Press 'q' to quit")
    #Make a variable called userScore and cpuScore to track scores, set to 0
    userScore = 0
    cpuScore = 0
    #LOOP:Make a round loop that continues while the userSCore or cpuSCore is less than 2
    while(userScore < 2 and cpuScore < 2):
        #Use input() to get a choice from rock paper scissors, q
        #Store the choice in a variable. Use .lower() to make users choice 
        userChoice = input("Please choose(Rock, Paper, Scissors): ")
        #make a list of choices, then use random.choice to get a random choice from cpu. Store choice in a variable
        cpulist = ["rock", "paper", "scissors"]
        cpuChoice = random.choice(cpulist)
        #Make an if/elif/else statement to check the user input against the cpu choice
        # I have to compare the user choice and cpu choice to rock, paper, and scissors separetely and combine with logical operators
        #operators.examplee of a tie
      
        if((userChoice == "rock" and cpuChoice == "rock") or (userChoice == "paper" and cpuChoice == "paper") or (userChoice == "scissors" and cpuChoice == "scissors")):
        
          
        #print("Draw")
            print("Draw") 
        #print("User:" + str(userScore) + "CPU:" + str(cpuScore))
        print("User:" + str(userScore) + "CPU:" + str(cpuScore))  
        #if the user won, add one to the users score, then print out the scores
        #"User: [#], CPU: [#]"
        if((userChoice == "rock" and cpuChoice == "scissors") or (userChoice == "paper" and cpuChoice == "rock") or (userChoice == "scissors" and cpuChoice == "paper")):
            userScore = userScore + 1
            print("User" + str(userScore) + "CPU:" + str(cpuScore)) 
        #else if (elif) the computer won, add one to the computer's score, then
        #print out the scores...
        elif((userChoice == "rock" and cpuChoice == "paper") or (userChoice == "scissors" and cpuChoice == "rock") or (userChoice == "paper" and cpuChoice == "scissors")):
            cpuScore = cpuScore + 1      
        #else if it is a draw, print("DRAW") then print out the scores...
        elif((userChoice == "rock" and cpuChoice == "rock") or (userChoice == "paper" and cpuChoice == "paper") or (userChoice == "scissors" and cpuChoice == "scissors")):
                print("Draw")
                print(str(userScore) + str(cpuScore)) 
        #else if the user enter 'q', then end the round, and the game loop
        #use the break statement to end the round. Make keepPlaying = False
        elif input("q"):
            break
            keepPlaying = False
                  

        #else the user didn't enter an accepted input, print "Not an option, try again"
    else:
        print("not an option try again")    
    #print thank you message
    print("Thanks for playing")
    #print out who won:
    
    #if the user score is 2, then the user won
    if(userScore == 2):
        print("You won!") 
    
    #elif the cpu score is 2, then the cpu won
    elif(cpuScore == 2):
        print("CPU won!")
    #print out the final scores
    print((cpuScore), (userScore))