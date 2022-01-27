#def future():
    #age = eval(input("enter your age:"))
    #futureage = age + 20
    #print("in 20 years you will be", futureage)


#def convert():
    # get user input in celsius (This is a comment)
    #celsius = eval(input("enter temp in celsius:"))
    #fahrenheit = celsius * 9 / 5 + 32

#display result to user
#print("that is", fahrenheit, "degrees fahrenheit")


#print("hello", end="")


#print("world")


#name, age = eval(input("hello!\nEnter your name and age: "))
#print("good to see you", name),"you are", age, "years old!")


#hour, minute = eval(input("Enter the hour and minute: "))
#print("it is", hour, ":", minute)


#for element in range(10):
#print(element, end=" ")


#principal =eval(input("enter principal balance: "))
#apr = eval(input('enter interest rate: '))
#for i in range(10):
#   principal = principal * (1+apr)
#  print(principal)
#print("the final balance is ", principal)

# for i in range(5):
#    for j in range(5):
#         print(i, j, end='-')
#     print()

import math

# dot notation
# x = math.sqrt(9)
# print(x)
# x = math.pow(2, 3) # parameters / arguments
# print(x)
# x = 2.0 ** 3
# print(x)


# my_range = range(10) # stop - default start 0, default step 1
# my_range = range(3, 10) # (start, stop) default step 1
# my_range = range(3, 10, 2) # (start, stop, step)
# my_range = range(10, 3, -1)
# print(list(my_range))

# accumulator pattern
# my_sum = 0
# for i in range(101):
#     my_sum = my_sum + i
# print(my_sum)

user_input = eval(input("Enter a number: "))
fact = 1
for i in range(user_input, 0, -1):
    fact =  fact * i
print(fact)