# this programe puts 10 random numbers into a que
# then take out 1st number and print the que list
# and so on until list is emply and prints " the q is now emply"

import random
queue = []
numberOfNumbers = 10
rangeTo = 100

for n in range(0, numberOfNumbers):
    queue.append(random.randint(0, rangeTo))
print("queue is {}" .format(queue))

while len(queue) != 0:
    currentNumber = queue.pop(0)
    print("current number is {} and the queues is {}" .format(currentNumber, queue))
print("queue is now emply")

