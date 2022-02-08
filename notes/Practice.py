#def future():
    #age = eval(input("enter your age:"))
    #future_age = age + 20
    #print("in 20 years you will be", future_age)


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

# user_input = eval(input("Enter a number: "))
# fact = 1
# for i in range(user_input, 0, -1):
#     fact =  fact * i
# print(fact)
#
# import math
#
# def quadratic_formula():
#     a, b, c = eval(input("enter coefficients a, b, and c:"))
#     sqrt_discr = math.sqrt(b * b -4 * a * c)
#     denom = 2 * a
#     root_1 = (-b + sqrt_discr) / denom
#     root_2 = (-b - sqrt_discr) / denom
#     print('root 1:', root_1, 'root 2:', root_2)
#
# from graphics import Point, GraphWin, Circle
# import math
#
# win = GraphWin('Face', 700, 700)
# face = Circle(Point(350, 100), math.pow(10, 2))
# left_eye = Circle(Point(310, 60), 25)
# right_eye = Circle(Point(390, 60), 25)
#
# face.draw(win)
# left_eye.draw(win)
# right_eye.draw(win)
# p = Point(50, 60)
# p.getX()
#
# p.getY()
# win = GraphWin()
# p.draw(win)
# p2 = Point(140,100)
# p2.draw(win)

from graphics import Point,GraphWin,Circle
win = GraphWin('Shapes')
center = Point(100,100)
circ = Circle(center, 30)
circ.setFill('red')
circ.draw(win)