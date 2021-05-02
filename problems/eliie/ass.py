# WAP to print the sum of prime numbers (using lambda function) up to n where n is the range defined by the user
n = int(input("enter a number : "))
import time
start_time = time.time()
n = n + 1
nums = range(2, n)   #:TODO:define what is nums
for i in range(2, n):# lambda parameter : action you want to perform , parameter (set on which action is to be
    # performed 
    nums = list(filter(lambda x: i == x or x % i, nums)) # i=2, nums= 2,3,4,5,6,7,8,9,10
    # after num=2,3,5,7,9

print(sum(nums))
print(time.time() - start_time)