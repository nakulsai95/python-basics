# WAP to print the sum of prime numbers (using lambda function) up to n where n is the range defined by the user
n = int(input("enter a number : "))
nums = range(2, n+1)
for i in range(2, n+1):# lambda parameter : action you want to perform , parameter (set on which action is to be
    # performed
    print(i)
    print("Before applying lambda ", nums)
    nums = (list(filter(lambda x: i == x or x % i, nums))) # i=2, nums= 2,3,4,5,6,7,8,9,10
    # after num=2,3,5,7,9
    print(nums)
# print(nums)
print(sum(nums))