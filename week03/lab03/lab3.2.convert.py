# convert float amount of dolars into cents
# eg 9.44 dolars = 944 cents

dolars = float(input('Please enter an amount :'))
cents = int(abs(dolars*100))

print('That amount in cent is : {}' .format(dolars, cents))

