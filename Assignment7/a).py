n = 5

# Upper half
for i in range(n):
    for j in range(2 * n - 1):
        if j == n - 1 - i or j == n - 1 + i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Lower half
for i in range(n - 2, -1, -1):
    for j in range(2 * n - 1):
        if j == n - 1 - i or j == n - 1 + i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
