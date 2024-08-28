for row in range(7):
    for col in range(7):
        if (row == 0) or (row == 6 and col <= 3) or (col == 3):
            print("*", end=" ")
        else:
            print(end="  ")
    print()


