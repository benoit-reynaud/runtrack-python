def draw_carpet(n):
    print("+---------+")
    for i in range(n+1):
        for j in range(n+1):
            if i == j:
                print("*", end="")
            elif i + j == n:
                print(" ", end="")
            else:
                print("*", end="")
        print()
    print("+---------+")
draw_carpet(10)