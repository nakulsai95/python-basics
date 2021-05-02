__author__ = 'nakulsai.adapala'
__date__ = '1May2021'
__version__ = 'python 3.6+*'

'''

Python basics covering functions, lambda functions and list comprehensions
'''
#
# def check_odd(x):
#     """
#     :param x: int
#     :return: boolean True/False
#     """
#     if x % 2 != 0:  # % indicates remainder of x and 2
#         return True  # return defines the output of function
#     else:
#         return False
#
# #
# y = lambda x: x % 2  # lamda is nothing but nameless function
# print(y(5))
#
#
# odd_numbers = [] #defined empty list
# numbers = list(range(4,8)) #defined numbers is a list of numbers starting 0 ending 7
# for number in numbers:  # iterating each element in list numbers
#     # print(number)
#     if number % 2 != 0 : #checking if number is if True, if False if numbers >5
#         odd_numbers.append(number) #appending element into list
#     else:
#         pass #else ignoring it
# # print(odd_numbers)
#
# odd_numbers = list(filter(lambda a: a%2 != 0, numbers)) #for a in numbers filter element when a%2 !=0
# odd_numbers = [a for a in numbers if a%2 != 0]  #list comprehension
# print(odd_numbers)
#
#
# numbers = [1,2,3,4,5,6,7,8]
#
# # print(x)
# # x.pop(3) #removes element
# # x.append() #add element at the end
# # x = [5] + x #add 5 at the start
# # x.reverse() #reverse all the elements in a list
# # x.sort()
# # print(x)
# # print(x.index(4))
# # print(len(x))
# #goal: i want only odd numbers
#
# # map
# # filter
# #
# # map
# # list u want to perform certain operation to every element
# #
# # filter u want add multiple conditions and filters out values from list
#
#
# number = 0
# a = lambda x: 1 if x > 0 else (-1 if x < 0 else 0)
# print(a(number))
#
#
# '''
# Step 1: list of numbers less than x
# Step 2: check if divivsable by any element less than x
# Step 3: add count if divisable
# Step 4: if count is grater than 2 its not prime
# Step 5: store all prime numbers into a list
# Step 6: take sum of all prime numbers
# '''



