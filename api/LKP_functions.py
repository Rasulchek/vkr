def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res


def find_factors(n):
    factors = set()
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors


def testprimitivedeg(a, p, e1, q, e2):
    a = int(a)
    p = int(p)
    q = int(q)
    e1 = int(e1)
    e2 = int(e2)
    m = (p**e1) * (q**e2)
    phi_val = m * (1 - 1/p) * (1 - 1/q)
    factors = find_factors(int(phi_val))
    for it in factors:
        if power(a, int(phi_val) // it, m) == 1:
            return False
    return True


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
    if d == 2 and i == 0:
        Ans.append([1, 1])
        return Ans
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
        if b % lf[i][0] != 0 and lf[i][0] != 1:
            test1 = False
    if m % 4 == 0 and b % 4 != 0:
        test2 = False
    if euclid(c, m) != 1:
        test3 = False
    return test1, test2, test3


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
