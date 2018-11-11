n = int(input("enter the number of rows "))
for row in range(n):
    for col in range(n):
        if (row+col==n//2 or col-row==n//2 or row-col==n//2 or row+col==(n+(n//2)-1)):
            print("*",end="")
        else:
            print(end="  ")
    print()
