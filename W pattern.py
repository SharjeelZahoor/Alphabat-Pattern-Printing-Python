for row in range(7):
    for col in range(9):
        if (col==0) or (col==8) or ((col==1 or col==7) and row==5) or ((col==2 or col==6) and row==4) or ((col==3 or col==5) and row==3) or (row == 2 and col == 4)  :
            print("*", end=" ")
        else:
            print(end="  ")
    print()
