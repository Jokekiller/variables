#Harry Robinson
#16-09-2014
#Fridge and Lift dimensions

print("This programme will take the dimensions of a fridge and see if it fits in a lift")
fridgeH = float(input("Give the fridge Height: "))
fridgeW = float(input("Give the fridge Width: "))
fridgeL = float(input("Give the fridge Length: "))
fridgeVolume = fridgeH*fridgeW*fridgeL
print("Fridge volume is {0}".format(fridgeVolume))
liftH = float(input("Give the lift Height: "))
liftW = float(input("Give the lift Width: "))
liftL = float(input("Give the lift Length: "))
liftVolume = liftH*liftW*liftL
print("Lift volume is {0}".format(liftVolume))
answer = float(liftVolume-fridgeVolume)
print("Amount of space left {0}".format(answer))
