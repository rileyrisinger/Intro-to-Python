#Guess the number game
#Riley Risinger
#March 1, 2020
#Computer randomly generates a number and then the user guesses, then told either too high or low

#import modules
import random

#get computer to randomly generate a number
com_num = random.randint(1,50)

#get user to guess number
guess_num = int(input("Pick a number from 1 to 50:"))

#compare chosen number to randomly generated number and generate response
while guess_num != com_num:
        if guess_num < com_num:
                print ("Too Low!")
        elif guess_num > com_num:
                print ("Too High!")
        guess_num=int(input("Try Again!:"))

#when they guess the number
print("Correct!")
