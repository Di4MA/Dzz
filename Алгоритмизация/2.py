def extended_euclidus(a, b):
    if a == 0:
        print("finished", b, 0, 1)
        return b, 0, 1

    nod, x1, y1 = extended_euclidus(b%a,a)

    x = y1 - b//a * x1
    y=x1
    print(a,b,x1,y1,x,y)
    return nod, x,y
