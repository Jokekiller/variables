#Harry Robinson
#15-09-2014
#A programme dividing numbers and giving their remainders

number1 = int(input("please give the first number: "))
number2 = int(input("please give second number: "))
answer = number1 // number2
remainder = number1 % number2
print(" Answer is {0} // {1} % {2}".format(number1, number2,answer,remainder))
