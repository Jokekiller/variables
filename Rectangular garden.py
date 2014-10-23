#Harry Robinson
#23-10-2014
#Rectangle garden

lengthOfGarden = float(input("Give the length of the garden: "))
widthOfGarden = float(input("Give the width of the garden: "))
areaOfGarden = (lengthOfGarden - 1) * (widthOfGarden - 1)
cost = areaOfGarden * 10
print("The cost is £{0}.".format(cost))
