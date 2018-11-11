n=int(input("enter the number of rows "))
for row in range(n):
    for col in range(n):
        if (row==0 or col==n-1 or col==row):
            print("*",end="")
        else:
            print(end="  ")
    print()
