def pascal(n, k):
    L = [1]
    for i in range(1, n+1):
        L.append(1)
        a = L[0]
        b = L[1]
        for v in range(1, i):
            L[v] = a + b
            a = b
            b = L[v+1]
    return L[k]