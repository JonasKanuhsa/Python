'''
Created on Mar 15, 2021

@author: ITAUser
'''
#Make a variable called score to keep track of the correct answers. And set
#it to 0.

#Ask the user question one. And store the users answer.

#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."

#Ask the user question two. And store the users answer.

#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."

#Ask the user question three. And store the users answer.

#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."

#Ask the user question four. And store the users answer.

#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."

#Calculate the percentage the user got. And store it in a variable called p

#Print out the users score: "You got a [score]/4. Or a [p]%."

Score = 0
A = "mitochondria" 
B = "nucleus"
C = "ribosome"
question1 = ("What is the power house of a cell? A.)mitochrondria, B.)nucleus, or C). ribosome" )
answer1 = input(question1)
if(answer1 == A):
    print("Correct")
else:
    print("Incorrect, the correct answer is A.")
if(answer1 == A):
    Score = +1
else:
    Score = +0

A = 13 
B = 45
C = 50
question2 = ("How many states are in the U.S? A).13, B). 45, C).50")
answer2 = input(question2)
if(input == C):
    print("Correct")
else:
    print("Incorrect, the correct answer is C.")
if(input == C):
    Score = +1
else:
    Score = +1


A = "Slope"
B = "Output"
C = "I dont uderstand math"
question3 = "In y=mx+b , what does m stand for?"
answer3 = input(question3)
if(input == A):
    print("Correct")
else:
    print("Incorrect, the correct answer is A.")
A = "Verb"
B = "Adjective"
C = "Noun"
question4 = "In English, a person, place or thing is called:A) verb B) adjective C) noun"
answer4 = input(question4)
if(input == C):
    print("Correct")
else:
    print("incorrect")
if(input == C):
    Score = +1
else:
    Score = +0



