for row in range(5):
    for col in range(5):
        if (col==0 or col==4):
            print("*",end="")
        elif (col==2 and row==2):
            print("*",end="")
        elif ((col==1 and row==1) or (col==3 and row==1)):
            print("*",end="")
        else:
            print(end="  ")
    print()
