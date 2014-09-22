#22/09/2014
#Hamza and Harry
#Currency problem

whole_number = int(input("Please enter the amount of money :"))

twenties = whole_number//20
remainder = whole_number%20

tens = remainder//10
remainder = remainder%10

fives = remainder//5
remainder = remainder%5

twos = remainder//2
remainder = remainder%2

print("Number of 20's {0}".format(twenties))
print("Number of 10's {0}".format(tens))
print("Number of 5's {0}".format(fives))
print("Number of 2's {0}".format(twos))
print("Number of 1's {0}".format(remainder))
