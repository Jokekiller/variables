#Harry Robinson
#22/09/2014
#Converting someones height and weight

print("This prgramme will convert your height and weight")
height = float(input("Give your height in inches; "))
weight = float(input("Give your weight in stones; "))

heightInCentimetres = height * 2.54
weightInKilograms = weight * 6.364

print("Your height in centimetres {0}".format(heightInCentimetres))
print("Your weight in kilograms {0}".format(weightInKilograms))
