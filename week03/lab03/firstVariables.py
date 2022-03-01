# messing around with variable types
# author: Ioan Domsa

ageOfPatient = {}
age = '3'

# we need to convert the type to str so we can concate it to the message
print ("type of ageOfpatient is :" + str(type(ageOfPatient)))
print ("type of age is:" + str(type(age)))

# show how to convert a str to int and int to str
print("you are " + str(age))
nextYear = int(age) + 1
print ("Next year you will be :" + str(nextYear))
