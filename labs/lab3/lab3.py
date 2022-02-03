"""
Andrew Turner
lab3.py

traffic monitoring code lab

"""

def traffic():
    numberofroads = eval(input("How many roads were surveyed?"))
    averageaccum = 0
    for road in range(1, numberofroads+1):
        print("How many days was road", road, "surveyed?")
        numberofdays = eval(input(" "))
        carsaccum = 0

        for day in range(1, numberofdays+1):
            print("How many cars were surveyed on day", day, "?")
            daycars = eval(input(" "))
            carsaccum = daycars + carsaccum
        averageaccum = carsaccum + averageaccum
        print("Road", road, "average vehicles per day:", carsaccum/numberofdays)
    print("Total number of vehicles on the road:", averageaccum)
    print("Average number of vehicles per road", round(averageaccum/numberofroads, 2))




