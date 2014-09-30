#Harry Robinson
#25-09-2014
#Programme calculating the volme of a pool with different depths

print("This program will calculate the volume of a pool with different depths")
shallowEndDepth = float(input("Give the shallow end depth: "))
deepEndDepth = float(input("Give the deep end depth:"))
width = float(input("Give the width of the pool: "))
length = float(input("Give the length of the pool: "))
differenceInDepth = deepEndDepth - shallowEndDepth
volumeOfSlopedBottom = (differenceInDepth * width * length)/2
volumeOfPool = volumeOfSlopedBottom + (length * width * shallowEndDepth)
volumeOfWater = volumeOfPool
print("The amount of water required is {0}".format(volumeOfPool))
