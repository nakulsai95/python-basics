'''
Conatins all the math functions required for project
'''

import math


__all__ = ['check_even', 'chcek_prime', 'find_mean', 'standard_deviation']

def check_even(x:int):
    '''
    Fucntion to detect if number is even or not
    
    x: int
    returns boolean
    '''
    if x % 2 == 0:
        return True
    else:
        return False

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

def find_mean(x):
    '''
    x: list
    '''
    mean = sum(x)/len(x)
    return mean

def standard_deviation(data):
    '''
    data: list of values
    '''
    n = len(data)
    mean = sum(data) / n
    return math.sqrt(sum((x - mean) ** 2 for x in data) / n)



    
    