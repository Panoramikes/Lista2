#3 write a function which takes an array of numbers as an input and finds the lowest value.
# Return the index of that element and its value (1p)

def the_lowest(matrix):
        komunikat=str("wartość, pozycja")
        array=matrix;
        def lowest(array): #funkcja znajdujaca najmniejsza wartosc w tablicy (1xn)
            a=len(array)
            n=0; #position in array
            min=float("inf");
            for i in range (0,a): #sprawdzenie wszytskich elementow macierzy 1xn
                if min>array[i]:
                    min=array[i];
                    n=i+1;
            return (min,n)

        z=len(array);
        try: #sprobuj jesli policzylo ilosc wierszy
            zz=len(array[0])
            answer=[]; #macierz na najnizsze wartosci z kazdej macierzy
            for j in range (0,z):
                 answer.append(lowest(array[j])); #wpisz wynik dla kazdej podtablicy 1xn
            minimum=float("inf")
            for k in range (0,z): #sprawdz ktory najnizszy wynik 'lokalny' (1xn) jest najnizszy 'globalnie' (mxn)
                tulpe=answer[k]
                spr=tulpe[0];
                poz=tulpe[1];
                if (spr < minimum):
                    minimum = spr
                    kk=k+1
                    pozycja_minimum=k*zz+poz
            pozycja_w_macierzy=[]
            pozycja_w_macierzy.append(poz) # nr kolumny wyniku
            pozycja_w_macierzy.append(kk)  # nr wiersza wyniku
            return print(komunikat),print(minimum, pozycja_minimum)
        except: #jesli nie to wykonaj dla ilosc_wiersz=1
            print(komunikat)
            print(lowest(array))

# X=[2,6,-3,0,1,-14,3,6,2,4,0.47,-1.13]
#
# Y=[[2,5,8,2],
#    [0,-6,11,8],
#    [7,-9,2,1]]
#
# Z=[[-1,0,0,-200,8,2,1],
#    [-1,0,0,2,8,2,1],
#    [-1,0,110,2,-998,20,1],
#    [-1,0,-2,2,-821,2,1]]
#
# A=[[2,1],[-9,-10]]
#
# B=[-111]
#
# the_lowest(X)
# the_lowest(Y)
# the_lowest(Z)
# the_lowest(A)
# the_lowest(B)
#the_lowest([[5,6],[-1,88]])

