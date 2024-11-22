import math
#sieve of Eratosthenes
def gen(num):
    prime = [True] * (num + 1)
    p = 2
    while p*p<=num:
        if prime[p]:
            for j in range(p*p,num + 1,p):
                prime[j] = False
            p += 1
    return [p for p in range(2,num+1) if prime[p]==True]
           
    
print(gen(21))
    
    
    