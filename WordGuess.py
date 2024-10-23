import random

print('WORD GUESSING GAME')
name = str(input('Enter name: '))
print('WELCOME'+' '+ name.upper())


words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)         

chances = 4
guessed = set()
while chances > 0:
    chances -=1

    w  = str(input('Enter a word, '+ f'hint is {word[:3]}:'))
    if w==word:
        print('BRAVO!')
        break
    elif len(w)==0 or not w.isalpha():
        print('ENTER VALID WORD')   
    elif chances==0 and w!=word:
        print(f'YOU LOOSE! ,word is {word}')  
    

      







        '''   
            character = str(input('Enter character: '))
            if not character.isalpha() or len(character)!=1:
                print('ENTER A VALID LETTER')
                continue

            if character in guessed:
                print('Already guessed')
                continue

            guessed.add(character)


            if character not in word: 
                print(f'Character not in word, hint ->{word[:3]}')
            else:
                print('Good guess')


            if all(char in guessed for char in word):
                print(f'CONGRATS  word is {word}')
                break
            elif chances == 0 and guessed != word:
                print('Lost')    '''
