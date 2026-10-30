#Sanke Water Gun game
import random #imports random module wich generates random iterations
'''
1 for snake
-1 for water
0 for gun '''

computer =random.choice([1, -1, 0]) #computer takes random choice between these numbers.
youstr = input("Enter your choice: ")
youDict = {"s":1, "w":-1, "g":0}#My dictonary assignrd to numbers
reverseDict = {1: "Snake", -1: "Water", 0:"Gun"}#dictnory is reversed, numbers assigned to respective choice.

you = youDict[youstr]

#By now we have 2 variables, you and computer

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("It's a draw!")

else:
    if(computer == -1 and you ==1):
        print("You win!")
    elif(computer == -1 and you ==0):
        print("You Lose!")
    elif(computer == 1 and you == -1):
        print("You lose!")
    elif(computer == -1 and you ==0):
        print("You win!")
    elif(computer == 0 and you ==-1):
        print("You win!")
    elif(computer == 0 and you ==1):
        print("You Lose!")
    else:
        print("something went wrong")