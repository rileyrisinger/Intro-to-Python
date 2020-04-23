import random

options = ["rock","paper","scissors"]
computer = random.choice(options)
user = input("Pick either rock, paper or scissors: ")


if user == 'rock':
    if computer == 'Rock':
        print('Tie Game')
    elif computer == 'Paper':
        print('You lose')
    else:
	print('You win!')
if user == 'paper':
    if computer == 'Rock':
        print('You win!')
    elif computer == 'Paper':
        print('Tie Game')
    else:
	print('You lose')
if user == 'scissors':
    if computer == 'Rock':
        print('You lose')
    elif computer == 'Paper':
        print('You Win!')
    else:
	print('Tie Game')

