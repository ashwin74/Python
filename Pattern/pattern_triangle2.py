n=int(input('enter no of rows '))
for i in range(n):
    for j in range(0,n-(i+1)):
        print(end=' ')
    for k in range(0,i+1):
        print('*', end=' ')
    print()

#optimized way same problem
#for i in range(n):
#    print(' '*(n-i-1)+"* "*(i+1))
