# program that reads in two numbers and 
# outptuts the integer answer and reminder

x = int(input('Enter first number :'))
y = int(input('Enter seccond number :'))
answer = x//y   # // gives the int division
reminder = x%y  # % give the remainder

print('{} divided by {} is {} with reminder {}' .format(x, y, answer, reminder))
