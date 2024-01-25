def eratosthenes(n):
    arr = lst(range(2, n))
    for i in range(len(arr)):
        if [i] != 0:
            p = arr[i]
            for j in range(2*p, len(arr),p):
                arr[j] = 0
    ans = []
    for i in range(len(arr)):
        if arr[i] !=0:
            ans.append(arr[i])
print(eratosthenes(10**3))
выучить все эти алгоритмы!!!!