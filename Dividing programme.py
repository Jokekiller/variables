#Harry Robinson
#16-09-2014
#Dividing programme

#Showing the remainder
print("This programme will divide two numbers and display the answer and the remainder")
number1 = int(input("Give the first number: "))
number2 = int(input("Give the second number: "))
answer = int(number1 / number2)
remainder = number1 % number2
print("Answer is {0} % {1} is {2} remainder {3}".format(number1, number2, answer, remainder))

#showing just the integer and more user friendly
print("This programme will divide two numbers and display the answer and the remainder")
number1 = int(input("Give the first number: "))
number2 = int(input("Give the second number: "))
answer = int(number1 // number2)
print("Answer is {0}".format(answer))
