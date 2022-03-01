# test format of an if statement



if False: 
    # statements
    print ("condition is true")
b = 2
if 2 == 2:
    print("b is equal to 2")
else: 
    print("b is not equal to 2")
a = 2
if a != 2:
    print ("I hope this is not displayed")
else:
    print ("2 is not equal to 2 is false")

aNumber = 5
if (aNumber % 2) == 0: # don't need brackets, in for clarity
    print (aNumber, "is even") # another way of printing variables
elif(aNumber % 3) == 0: # if the number is even this will not be checked
    print (aNumber,  "is divisble by 3")
else:
    print(aNumber, "is not even or divisble by 3")
