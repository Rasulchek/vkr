import random


def bbs_generator(p, q, seed, l):
    p = int(p)
    q = int(q)
    print(p, q)
    seed = int(seed)
    l = int(l)

    n = p * q
    x = seed
    L = str()
    for i in range(0, l):
        x = x ** 2 % n
        z = x % 2
        L += str(z)
    return L


def euclid(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return max(a, b)


def MillerRabinTest(n, t):
    def PowerModN(a, d, n):
        dbin = bin(d)[2:]
        b = 1
        for i in range(0, int(len(dbin))):
            b = (b ** 2) % n * a ** int(dbin[i]) % n
        return b


    def getrandom(n):
        digits = len(str(n))
        min_value = 10 ** (digits - 1)
        return random.randint(min_value, n)


    def iscomposite(a, n, r, s):
        flag = (euclid(a, n) != 1)
        if euclid(a, n) != 1:
            return True
        if PowerModN(a, r, n) == 1:
            return False
        for i in range(0, s):
            if PowerModN(a, (2 ** i) * r, n) == n - 1:
                return False
        return True

    N = n - 1
    # print(N)
    s = 0
    while (N) % 2 == 0:
        N = N // 2
        s = s + 1
    r = N
    for i in range(0, t):
        a = getrandom(n)
        if iscomposite(a, n, r, s):
            return False
        return True
