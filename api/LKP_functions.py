def Factor(n):
    Ans = []
    d = 2
    i = 0
    while n != 1:
        if n % d == 0:
            i += 1
            n //= d
        else:
            if i != 0:
                Ans.append([d, i])
            i = 0
            d += 1
    Ans.append([d, i])
    return Ans


def testprimitive(a, p, lf):
    m = p - 1
    for i in range(0, int(len(lf))):
        if a ** (m / lf[i][0]) % p == 1:
            return False
    return True


def euclid(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return max(a, b)


def test_multip_prim(a, c, m):
    a = int(a)
    m = int(m)
    c = int(c)
    test1 = True
    test2 = True
    test3 = True
    b = a - 1
    lf = Factor(m)
    print(lf)
    for i in range(0, len(lf)):
        if b % lf[i][0] != 0:
            test1 = False
    if m % 4 == 0 and b % 4 != 0:
        test2 = False
    if euclid(c, m) != 1:
        test3 = False
    return test1, test2, test3


def testprimitivedeg(a, p, e):
    a = int(a)
    p = int(p)
    e = int(e)
    lf = Factor(p - 1)
    if e == 1:
        return testprimitive(a, p, lf)
    else:
        for i in range(0, int(len(lf))):
            if a % p == 0 or (a ** (p ** (e - 1) * (p - 1) // lf[i][0])) % p == 1:
                return False
            else:
                if a ** (p - 1) % (p ** 2) == 1:
                    return False
    return True


def lkp_power(a, m):
    a = int(a)
    m = int(m)
    test = True
    b = a - 1
    j = 0
    lf = Factor(m)
    for i in range(0, len(lf)):
        if b % lf[i][0] != 0:
            test = False
    if test:

        while b**j % m != 0:
            j += 1
    return test, j


# расширенный алгоритм Евклида и возвращает НОД gcd и коэффициенты Безу x и y
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y


# нахождениe обратного элемента к а
def find_inverse(a, m):
    test = True
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        test = False
        a_inv = 0
    else:
        a_inv = x % m
    return test, a_inv


def calc_arbitrary_el(a, c, m, kn_el, kn_num, unkn_num):
    a = int(a)
    c = int(c)
    m = int(m)
    kn_el = int(kn_el)
    kn_num = int(kn_num)
    unkn_num = int(unkn_num)
    test, a_inv = find_inverse(a, m)
    if test:
        x_0 = (kn_el - (a ** kn_num - 1) * c // (a - 1)) * (a_inv ** kn_num)
        unkn_el = (a ** unkn_num * x_0 + (a ** unkn_num - 1) * c // (a - 1)) % m
    else:
        unkn_el = 0
    return test, unkn_el


def calculate_lkp(x, a, c, m, l):
    x = int(x)
    a = int(a)
    c = int(c)
    m = int(m)
    l = int(l)
    L = str()
    L += str(x)
    L += ", "
    for i in range(0, l):
        x = (a * x + c) % m
        # print x
        L += str(x)
        L += ", "
    return L
