n=int(input("enter the number of rows "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(j,end=" ")
    print()
