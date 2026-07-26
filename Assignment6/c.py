for i in range(1, 5):
    for j in range(1, 8):

        if j == 5 - i or j == 3 + i:
            print(1, end=" ")

        elif i == 3 and j == 4:
            print(2, end=" ")

        elif i == 4 and (j == 3 or j == 5):
            print(3, end=" ")

        else:
            print(" ", end=" ")

    print()