import random

print('NUMBER GUESSING GAME!')
l_b = int(input('Enter lower bound: '))
u_b = int(input('Enter upper bound: '))

number_range = random.randrange(l_b,u_b)
Maxnumber_of_guesses = 7
tries = 0

while tries < Maxnumber_of_guesses:
    tries += 1 
    num = int(input('Enter number: '))

    if num == number_range:
        print(f'Congrats, you got it in {tries} attempt') 
        break        
    elif tries == Maxnumber_of_guesses and num != number_range:
        print(f'sorry the number is {number_range}, better luck next time!')
    elif num > number_range:
        print('Try again! you guessed too high')
    elif num < number_range:
        print('Try again! you guessed too small') 

