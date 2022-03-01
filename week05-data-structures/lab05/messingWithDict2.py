# messing with dictionaries

from pandas import value_counts


car = { 
    "make" : "ford", 
    "model" : "Punto", 
    "price" : 10000, 
    "tags" : ["pre-owned", "Best-Buy", "Dealer"]
        
}

for key, value in car.items():
    print (key, "has a value", value)
