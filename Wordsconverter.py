# Define the lists
units = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
two_digits = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
ten_mul = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
ten_power = ["Hundred", "Thousand"]

number = int(input('Enter number btw(0-32767): '))
def ntw(number):
    if 0<=number<10:
        return(f'{units[number]}')
    elif 10<=number<20:
        return(f'{two_digits[number-10]}')
    elif 20<= number < 100:
        if number%10 != 0:
            return(f'{ten_mul[number//10]}-{ntw(number%10)}') 
        else:
            return(f'{ten_mul[number//10]}')          
    elif 100<=number < 1000:
        if number%100 != 0:
            return(f'{units[number//100]}-Hundred-and-{ntw(number%100)}')
        else:
            return(f'{units[number//100]}-Hundred')
    elif 1000<=number<32767:
        if number%1000!=0:
            return(f'{units[number//1000]}-thousand-{ntw(number%1000)}')          
        else:
            return(f'{ntw(number//1000)}-thousand')
    else:
        return 'Invalid'                
print(ntw(number))            