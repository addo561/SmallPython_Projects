from csv import reader
import numpy as np
from itertools import chain
import random

name_game = 'GUESSER!'

def wordbank(fileW):
    file = open(fileW,'r')
    readerw = reader(file)
    word_bank = []
    for w in readerw:
        w = [w.replace(' ','').split('.',1)[-1].lower() for w in w]
        word_bank.append(w)
        
    word_bank = list(chain.from_iterable(word_bank))
    return word_bank

word_bank = wordbank('wordGUesser2\word.txt')
random_choice = random.choice(word_bank)

misplaced_letters = []
gussed_inc_letters = []
max_turns = 5
cur_turns = 0
name = input('Name? ')
print(f'WELCOME {name},PLAY {name_game}\n There are 5 letters to guess and you have only 5 turns for that')

while max_turns >= cur_turns:
    cur_turns += 1
    guess = input('Type guess: ') 
    
    if len(guess)!=len(random_choice) or guess.isalpha() is False:
        print('word should have 5 characters and should be letters')
        continue
    
    guess.lower()
    index = 0
    while index < len(guess):
        if guess[index] == random_choice[index]:
            print(f'{guess[index]}',end='')
            if guess[index] in misplaced_letters:
                misplaced_letters.remove(guess[index])  
        elif guess[index] in random_choice:
            print('_',end='')
            if guess[index] not in misplaced_letters:                
                misplaced_letters.append(guess[index])
        else:
            if guess[index] not in random_choice:
                print('_',end='')
                if guess[index] not in gussed_inc_letters:
                    gussed_inc_letters.append(guess[index])
        index += 1
            
    print(f' Misplaced letters -> {misplaced_letters}')
    print(f'Incorrect guessed words -> {gussed_inc_letters}')
    
    if guess==random_choice:
        print('You Won')
        break
    elif  cur_turns==max_turns:
        print('turns run out  you lost,  word is ',random_choice)
        break
    
    print('You have '+ str(max_turns - cur_turns) + 'turns left')

                
        
        
    
       