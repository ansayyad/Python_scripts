#This program is to guess the random number

import random

print('Hello, What is your name:')
name=input()

print('Well '+name+' I am thinking to guess a number between 1 to 20')

secretnumber=random.randint(1,20)

for i in range(1,7):
    print('Enter your guess:')
    guess = int(input())
    if guess < secretnumber:
        print('Your guess is too low')
    elif guess > secretnumber:
        print('Your guess is too high')
    else:
        break
if guess == secretnumber:
    print('Good Job '+name+' You have guessed my number in ',i , '  attempts')
else:
    print('Nope! The number i was thinking of '+str(secretnumber))
