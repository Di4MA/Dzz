def euclidus (n, m):
    while m%n > 0:
        m, n=n, m%n
    return n
euclidus (48, 24)