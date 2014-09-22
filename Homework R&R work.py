#Harry Robinson
#11/09/2014
#This is a prgramme of adding three numbers
print("This program will ask for 3 numbers and give the total added together")
num1 = int(input("Give the first number: "))
num2 = int(input("Give the second number: "))
num3 = int(input("Give the third number: "))
ans = num1 + num2 + num3
print ("The total is {0} + {1} + {2} is {3}".format(num1,num2,num3,ans))

           
print("This programme will ask for two integers and multiply them together")
num1 = int(input("Give the first number: "))
num2 = int(input("Give the second number: "))
ans = num1 * num2
print ("The total is {0} * {1} is {2}".format(num1,num2,ans))

print("This programme will work out the volume of a reatngular swimming pool")
poolH = float(input("Give the Height of the pool: "))
poolL = float(input("Give the Length of the pool: "))
poolW = float(input("Give the Width of the pool: "))
#this uses a float not an int because you could be dealing with decimal numbers and int numbers dont allow that.
ans = poolH * poolL * poolW
print ("The volume of the pool is {0} * {1} * {2} is {3}".format(poolH,poolL,poolW,ans))
