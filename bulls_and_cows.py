import random
print('START GUESSING GAME⬇️')

def list0fnums(num):
    return [ int(x) for x in str(num)]

def generatenum():
    while True:
        numGen = random.randrange(1000,9999)
        if Noduplicate(numGen):
            return numGen


def Noduplicate(num):
    l1 = list0fnums(num)
    if len(l1) == len(set(l1)):
        return True
    return False


def bull_cows(num,guess):
    bull_cow = [0,0]
    num_list = list0fnums(num)
    guess_list = list0fnums(guess)

    for i,j in zip(num_list,guess_list):

        if j in num_list:
            if i == j :
                bull_cow[0] +=1
            bull_cow[1] +=1   
    return bull_cow         


num = generatenum()    
tries = 3

while tries>0:
   
    num_user = int(input('Enter guess: '))
    if num_user < 1000 or num_user > 9999:
        print('Try again too large, number between 1000 and 9999')
        continue

    if not Noduplicate(num_user):
        print('Start over number have duplicates')
        continue

    bull_cow = bull_cows(num,num_user)
    print(f'bull: {bull_cow[0]} and cows:{bull_cow[1]}')
    tries -=1

    if bull_cow[0]==4:
        print('YOU WON!')
        break
    if tries ==0:
        print(f'SORRY GAME OVER NUMBER IS {num}')  
    
