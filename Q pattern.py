
for row in range(7):
    for col in range(7):
        if (row == 0) or (row == 6) or (col == 0) or (col == 6) or (col == 4 and row == 4) or (col == 5 and row == 5):
            print("*", end=" ")
        else:
            print(end="  ")
    print()
