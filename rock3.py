import random

options = ["Rock","Paper","Scissors"]
computer = random.choice(options)
user = raw_input("Pick either Rock, Paper or Scissors: ")
user = user.lower()
if user == 'rock' or 'paper' or 'scissors':
    print "The computer has drawn %s whilst you have drawn %s " % (computer,user)
if user == 'rock':
    if computer == 'Rock':
        print 'Tie Game'
    elif computer == 'Paper':
        print 'You lose:('
    else:
        print 'You win!'
if user == 'paper':
    if computer == 'Rock':
        print 'You win!'
    elif computer == 'Paper':
        print 'Tie Game'
    else:
        print 'You lose:('
if user == 'scissors':
    if computer == 'Rock':
        print 'You lose:('
    elif computer == 'Paper':
        print 'You Win!'
    else:
        print 'Tie Game'
