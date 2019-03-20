#0 Use alternative way of reading inputs - using library (0.5p)

#alternative way of reading inputs - using library:
#in terminal/command line write pip install cs50
#restart your IDE (Pycharm, VSCode, whatever it is)
#remember to use python3 in your project
#add "from cs50 import get_int" to the top of your file
# x = get_int("x: ")
# y = get_int("y: ")

from cs50 import get_int
try:
    print("enter value x: ")
    x = get_int("x: ")
    print("enter value y: ")
    y = get_int("y: ")
except:
    print("enter proper value")

