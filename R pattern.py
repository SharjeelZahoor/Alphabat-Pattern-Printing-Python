
for row in range(7):
    for col in range(7):
        if col == 0 or (col == 6 and (row < 3 and row > 0)) or (row == 0 and col < 6) or (row == 3 and col < 6) or (row == 4 and col == 1) or (row == 5 and col == 3) or (row == 6 and col == 5):
            print("*", end=" ")
        else:
            print(end="  ")
    print()
