def generate_pascal_triangle(n):
    result = [[1] *(i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            # Sets this entry to the sun of the two above adjacent entries
            result[i][j] = result[i-1][j-1] + result[i - 1][j]
    return result