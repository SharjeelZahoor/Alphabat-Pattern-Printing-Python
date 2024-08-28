
for row in range(7):
    for col in range(7):
        if (row == 6 and (col > 0 and col < 6)) or (col == 0 and (row < 6)) or (col == 6 and row < 6):
            print("*", end=" ")
        else:
            print(end="  ")
    print()
