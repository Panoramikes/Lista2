#1  (1p)Perimeter & field of circles with given radius X for the first circle & Y for the second one.
import numpy as np
warunek=0
try:
    while warunek == 0:
        print("Enter first radius")
        x=float(input())
        if x>0:
            warunek=1
        else:
            print("radius must be greater than zero")
    while warunek == 1:
        print("Enter second radius")
        y=float(input())
        if y>0:
            warunek=0
        else:
            print("radius must be greater than zero")
    pi=np.pi
    field_of_the_circleX=np.pi*x**2
    perimeter_of_the_circleX=2*np.pi*x
    field_of_the_circleY=np.pi*y**2
    perimeter_of_the_circleY=2*np.pi*y
    print("field of the circle X: ")
    print(field_of_the_circleX)
    print("perimeter of the circle X: ")
    print(perimeter_of_the_circleX)
    print("field of the circle Y: ")
    print(field_of_the_circleY)
    print("perimeter of the circle Y: ")
    print(perimeter_of_the_circleY)
except:
    print("Something gone wrong, radius must be a real, positive number")