# This program reads in a student percentage
# and prints out the corresponding grade

import math
percentage = math.ceil(float(input("Enter the percentage :")))
# print percentage

# be careful with ands and ors

if (percentage < 0) or (percentage > 100) :
    # This should really trow an error
    print ("Please enter a number between 0 and 100 ")
elif percentage < 40 : # we know it is greater than 0
    print ("Fail")
elif percentage < 50 : # between 40 and 49
    print ("Pass")
elif percentage < 60 :
    print ("Merit1")
elif percentage <70 :
    print ("Merit2")
else :
    print ("Distinction")