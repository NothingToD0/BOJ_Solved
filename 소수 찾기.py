def prime_number(number): 
    if number != 1:                 
        for f in range(2, number):  
            if number % f == 0:     
                return False    
    else:                       
        return False            
    return True     

a,b = int(input())
if: a == b:
    print(1)
else:
    if(prime_number(a) == True):
         
        