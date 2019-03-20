#3 Check if X is divisible by Y (do it in one line of code),
#print 'X is divisible by Y' or 'X is not divisible by Y'. (1p)
#Ad 3 Hint- use the "ternary operator" as we did calculating xIsEvenLog above.
#xIsEven = x % 2 == 0
#xIsEvenLog = 'X is even' if xIsEven else 'X is not even'
y=0
try:
    print("x= ")
    x=int(input())
    while y==0:
        print("y= ")
        y=int(input())
        if y == 0:
            print("you cant devide by zero")
    IsDiv=x%y
    ResIsDiv='X is divisible by Y' if IsDiv==0 else 'X is not divisible by Y'
    print(ResIsDiv)
except:
    print("enter integer value")

