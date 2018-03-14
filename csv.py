from random import randint
import random

# dataset
numOfRows = 20 # the number of rows that will be created

airlinesCodes = ["BA", "LH", "IB", "EY", "BE"]
airlines = ["British Airways", "Lufthansa", "Iberia Airlines", "Etihad Airline", "Flybe"]
classes = ["economy", "business", "first"]
airports = ["LHR", "SVO", "CDG", "LGW" ,"JFK", "LAX", "BCN", "LCY", "AMS", "BER"]

# ensures the departure airport is different from the destination
def destAirport(col2):
    x = airports[randint(0, len(airports)-1)]
    if x == col2:
        return destAirport(col2)
    else:
        return x

file = open("flightdata.txt","w+")

for i in range(1, numOfRows):
    randAirline = randint(0, len(airlinesCodes)-1)
    col1 = airlinesCodes[randAirline] + str(randint(100, 999))
    col2 = airports[randint(0, len(airports)-1)]
    col3 = destAirport(col2)
    col4 = str(randint(1000, 123123))
    col5 = str(randint(0, 11)) + str(randint(0, 59))
    col6 = str(randint(0, 11)) + str(randint(0, 59))
    col7 = airlines[randAirline]
    col7 = str(randint(10, 3000)) + "." + str(randint(1, 99))
    col8 = str(classes[randint(0, len(classes) -1)])

    file.write(col1 + ", " + col2 + ", " + col3 + ", " + col4 + ", " + col5 + ", " + col6 + ", " + col7 + ", " + col8 + "\n")

file.close()
