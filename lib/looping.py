#!/usr/bin/env python3

def happy_new_year():
   i = 10
   while i >= 1:
      print(i)
      if i == 1: 
         print('Happy New Year!')
      i -= 1
  
  
def square_integers(int_list):
    return_this = [num * num for num in int_list]
    return return_this

# def fizzbuzz():
#    i = 1
#    while i < 100:
#       print(i)
#       if i % 3 == 0 and i % 5 == 0:
#          print("FizzBuzz")
#       elif i % 3 == 0: 
#          print('Fizz')
#       elif i % 5 == 0:
#          print('Buzz')
#       i += 1

def fizzbuzz():
   i = 1
   while i <= 100:
      if i % 3 == 0 and i % 5 == 0:
         print("FizzBuzz")
      elif i % 3 == 0: 
         print('Fizz')
      elif i % 5 == 0:
         print('Buzz')
      else:
         print(i)
      i += 1