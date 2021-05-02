__author__ = 'citizen'
'''
Code to find sum of prime numbers less than x where x is user given
'''

x =int(input("Enter the number: "))
import time
start_time = time.time()
# pnos=[]  #:TODO: no need to defined if used lamda fucntion
def check_prime(x):
    '''
    x: int 
    returns: bool True if prime None if not
    '''
    for i in range(2,x):
        if(x % i==0):
            break
    else:
        return True

# for i in range(2,x):
#   if prime(i):
#     pnos.append(i)


    
natural_numbers = range(2,x) 
pnos = list(filter(lambda x: check_prime(x), natural_numbers))
sum_of_pnos = sum(pnos)

print(sum(pnos))
print(time.time() - start_time)
#ignore 1, 1 is not prime number 


'''
logic is easy to understand
No comemnts but variable names are easy to understand
No lambda functions used
'''