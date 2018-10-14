a=input('enter a string ')
length = len(a)
for i in range(length):
    for j in range(i+1):
        print(a[j],end=' ')
    print()
