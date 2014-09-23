#Harry Robinson
#23-09-2014
#programme dividing the amounts of weights up between an amount
print("This program will calculate the number of different weights required to balance one mass")
totalWeight = int(input("Give the total weight as an integer: "))
numberOfHundreds = totalWeight // 100
remainder = totalWeight % 100
numberOfFiftys = remainder // 50
remainder = remainder % 50
numberOfTens = remainder // 10
remainder = remainder % 10
numberOfFives = remainder //5
remainder = remainder % 5
numberOfTwos = remainder // 2
remainder = remainder % 2
numberOfOnes = remainder 
print("Number of 100grams needed {0}".format(numberOfHundreds))
print("Number of 50grams needed {0}".format(numberOfFiftys))
print("Number of 10grams needed {0}".format(numberOfTens))
print("Number of 5grams needed {0}".format(numberOfFives))
print("Number of 2grams needed {0}".format(numberOfTwos))
print("Number of 1grams needed {0}".format(numberOfOnes))
