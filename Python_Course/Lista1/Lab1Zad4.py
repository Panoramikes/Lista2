#4 looking at lab1-input and lab1-plot files create your own python script that takes
# a number and returns any chart of a given length.
#the length of a chart is the input to your script. The output is a plot
# (it doesn't matter if it's a y=x or y=e^x+2x or y=|x| function, use your imagination)
#test your solution properly. Look how it behaves given different input values. (1p)
from numpy import *
from numpy.random import *
from matplotlib.pyplot import *


def draw(a,b): #a,b - przedzial rysowania
    przedzial_x=linspace(a,b,100) #100 wartosci x, pomiedzy poczatkiem i koncem zadanego przedzialu
    def y(x):
        output=0.23*x**3 - 2*x**2 + 3*x - 17 #przykładowa funkcja
        #output=exp(x)
        #output=absolute(x)
        return output
    figure(1, figsize=(8, 6)) #wielkosc wykresu
    xlabel('x')
    ylabel('f(x)')
    return plot(przedzial_x,y(przedzial_x)), show() #rysowanie wykresu f(przedzial_x)=y=output
#a=randint(-10,10) #losowy przedzial
#b=randint(-10,10)
#a=0;
#b=400;
#draw(a,b)
draw(-100,100)




