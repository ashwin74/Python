for row in range(7):
    for col in range(6):
        if (col==0 or (row==0 and col !=5) or (row==6 and col!=5)):
            print("*",end="")
        elif (col==4 and (row>2 and row<6)):
            print("*",end="")
        elif (row==3 and (col==3 or col==5)):
            print("*",end="")
        else:
            print(end="  ")
    print()
