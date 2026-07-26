for i in range(1, 6):

    # Print leading spaces
    for j in range(1, 6 - i):
        print(" ", end=" ")

    # Print alphabets
    ch = 65
    for j in range(1, 2 * i):
        print(chr(ch), end=" ")
        ch += 1

    print()