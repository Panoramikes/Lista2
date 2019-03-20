#4 Add rounding for the above x/y operation.
# Round to 2 decimal points.
# Hint: look up in Google "python limiting number of decimals". (1p)
# In case of task 4  do not forget to round to different amount of decimals and see if it still works.
y=0
a=2
try:
    print("x= ")
    x=float(input())
    while y == 0:
        print("y= ")
        y=float(input())
        if y==0:
            print("you cant devide by zero")
    wynik=x/y
    print("%.2f" % round(wynik,a))
except:
    print("enter proper value")
  # >>> a=13.946
  # >>> print(a)
  # 13.946
  # >>> print("%.2f" % a)
  # 13.95
  # >>> round(a,2)
  # 13.949999999999999
  # >>> print("%.2f" % round(a,2))
  # 13.95
  # >>> print("{0:.2f}".format(a))
  # 13.95
  # >>> print("{0:.2f}".format(round(a,2)))
  # 13.95
  # >>> print("{0:.15f}".format(round(a,2)))
  # 13.949999999999999