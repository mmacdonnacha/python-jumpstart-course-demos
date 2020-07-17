import random


print('------------------------------------------')
print('          GUESS THE NUMBER APP')
print('------------------------------------------')
print()

randomNumber = random.randint(0, 100)
user_guess = int(input('Guess a number between 0 and 100: '))


while user_guess != randomNumber:
    if user_guess < randomNumber:
        print('Sorry but {} is LOWER than the number.'.format(user_guess))
    else:
        print('Sorry but {} is HIGHER than the number.'.format(user_guess))
    
    user_guess = int(input('Guess a number between 0 and 100: '))

print('YES! You\'ve got it. The number was {}'.format(user_guess))