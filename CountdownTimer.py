import time
count = int(input('Enter length of countdown in seconds: '))

def countdown(t):
    while t: # loop until t ==0
        minit, seconds = divmod(t,60) #if t = 10 minnit = 0,sec=10 and so on
        timer = f'{minit}:{seconds}'
        print('EXECUTION🔫')
        print(timer,end = "\r")
        time.sleep(1)
        t -= 1
    print('DONE!😆')

countdown(count)