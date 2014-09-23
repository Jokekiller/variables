#Harry Robinson
#23-09-2014
#Program calculating volumes of swimming pools

print("This program calculates the volume of a particular shape of swimming pool.")
poolWidth = float(input("Give the Width of the pool: "))
poolLength = float(input("Give the Length of the pool: "))
poolDepth = float(input("Give the Depth og the pool: "))
mainSectionVolume = poolWidth * poolLength * poolDepth
circleRadius = poolWidth / 2
circleArea = 3.14 * (circleRadius * circleRadius)
halfCircleVolume = (circleArea/2)* poolDepth
poolVolume = mainSectionVolume + halfCircleVolume
print("Pool volume is {0}".format(poolVolume))
