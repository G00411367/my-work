# program that prints out a random number between 1 and 10

import random

num1 = int(input('enter first number of the range :'))
num2 = int(input('enter last number of the range :'))

number = random.randint(num1, num2)

print('here is a random number : {}' .format(number))

