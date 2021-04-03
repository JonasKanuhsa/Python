'''
Created on Apr 3, 2021

@author: ITAUser
'''
'''
For this assignment you should read the task, then below the task do what it asks you to do
based on what the task tells you do first.
EXAMPLE TASK:
'''
#EX) Declare a variable set to 3. Make a while loop that prints the variable 
#    you just created and decrements the variable by one each time through
#    the loop. Meanwhile, make the loop run until the variable you created 
#    equals 0.
i = 3;
while i > 0:
    print(i)
    i -= 1

'''
END OF EXAMPLE
'''

'''
START HERE
'''

'''While Loops'''
#1) Declare a variable set to 4. Make a while loop that prints the variable 
#    you just created and decrements the variable by one each time through
#    the loop. Meanwhile, make the loop run until the variable you created 
#    equals 1.
var1 = 4
while(var1 >= 1):
    print(var1)
    var1 = var1 - 1
    break

#2) Declare a variable set to 14. Make a while loop that prints the variable 
#    you just created and increments the variable by one each time through
#    the loop. Meanwhile, make the loop run until the variable you created 
#    equals 20.
x = 14
while(x <= 20):
    print(x)
    x = x + 1
    
#3) Declare a variable set to 55. Make a while loop that prints the variable 
#   you just created. Then make an if statement that makes the loop break when
#   the variable is equal to 50. 
y = 55
while(y == 55):
    print(y)
    y = y-1
    if(y == 50):
        break

'''For Loops'''
#4) Create a list named sports. Put three sports into the list. Create
#   a for loop that prints each sport in the list
sports = ["football","basketball","golf"]
for var2 in [sports]:
    print(var2)
    
#5) Create a for loop that loops through each letter in a string of one of your
#   favorite songs. Each iteration should print should a letter of the word. 
O = ["H","B","S"]
if (O == ["H","B","S"]):
    print(O)
#6) Create a list named movies. Put five of your favorite movies into the list.
#   However, make sure one of the movies is Avatar. 
#   Create a for loop that iterates over the list. In the loop print the movie
#   being looped over, but create an if statement that breaks out of the 
#   loop if it is Avatar.
movies = ["Cars","Holes","Joker","Avatar","Platoon"]
while(movies == ["Cars"],["Holes"],["Jokar"],["Avatar"],["Platoon"]):
    print(movies)
    if (movies == ["Avatar"]):
        break



