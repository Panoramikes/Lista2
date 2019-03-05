#2 ask the user for a number and print its factorial (1p)
try:
    condition=1;
    while condition == 1:
        print("Enter natural number: ")
        n=int(input())
        if n>=0: #pytaj dopoki uzytkownik wprowadza liczby ujemne
            def factorial(x):
                answer=1;
                for i in range(1,n+1):
                    answer=answer*i;
                return print("Factorial is: "),print(answer)
            factorial(n)
            condition=0;
        else:
            print("Number must be a positive integer")
except:
    print("Something gone wrong, remember that a number must be a positive integer")