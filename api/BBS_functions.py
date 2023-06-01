def bbs_generator(p, q, seed, l):
    p = int(p)
    q = int(q)
    print(p, q)
    seed = int(seed)
    l = int(l)

    n = p*q
    x = seed
    L = str()
    for i in range(0, l):
        x = x**2 % n
        z = x % 2
        L += str(z)
    return L