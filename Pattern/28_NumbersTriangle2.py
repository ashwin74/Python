n=int(input("enter the number of rows "))
k=n
for i in range(n,0,-1):
    for j in range(i):
        print(k,end=" ")
    print()
    k -= 1
