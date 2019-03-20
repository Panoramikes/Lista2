#2 Find X & Y that satisfy: X is divisible by Y and both X & Y are even. (0.5p)
try:
    print("X>Y, Want to enter Y: 1, if X enter: 2 ")
    print("1 or 2: ")
    u=int(input())
    if u==2:
        warunek=0
        while warunek==0:
            print("Enter even integer number: ")
            x=int(input())
            w=x%2
            if w==0:
                warunek=1;
            else:
                print("Its not even integer number")
        y=2
        stop=0;
        while x>=y and stop==0:
            z=y%2
            if z==0:
                wynik=x%y
                if wynik == 0:
                    stop=1
            if stop==0:
                y=y+1;
        print("X= ")
        print(x)
        print("Y= ")
        print(y)
    if u==1:
        warunek = 0
        while warunek == 0:
            print("Enter even integer number: ")
            y = int(input())
            w = y % 2
            if w == 0:
                warunek = 1;
            else:
                print("Its not even integer number")
        x=y+1
        warunek2=1
        while warunek2==1:
            w=x%y
            if w==0 :
                warunek2=0
            else:
                x=x+1
        print("X= ")
        print(x)
        print("Y= ")
        print(y)
except:
    print("Try again, its wrong value")