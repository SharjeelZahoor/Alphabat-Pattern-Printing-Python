for row in range(7):
    for col in range(5):
        if (row == 0 or row == 3 ) or ((col == 0) and ((row != 0) and (row != 3))):
            print("*", end=" ")
        else:
            print(end="  ")
    print()