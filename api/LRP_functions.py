from numpy.polynomial import Polynomial as Polynom
import numpy as np


def str_pol(s):
    a = list(map(int, str(s)))
    pol = Polynom(a)
    return pol


def ToStr(A):
    a = A.coef
    b = str()
    for i in range(a.shape[0]):
        b += (str(int(a[i])))
    return b


def odd(A):
    if type(A) == Polynom:
        a = A.coef
    else:
        a = A
    for j in range(a.shape[0] - 1, -1, -1):
        if a[j] == 1:
            b = a[:j + 1]
            break
        else:
            b = np.array([0])
    if type(A) == Polynom:
        return Polynom(b)
    else:
        return b


def sum_pol(A, B):
    if type(A) == Polynom:
        a = A.coef
        b = B.coef
    else:
        a = A
        b = B
    k = max(a.shape[0], b.shape[0])
    if a.shape[0] < k:
        c = np.zeros(k)
        c[:a.shape[0]] = a
        a = c
    if b.shape[0] < k:
        c = np.zeros(k)
        c[:b.shape[0]] = b
        b = c
    sum = np.ones(k)
    for i in range(k):
        if a[i] == b[i]:
            sum[i] = 0
    S = Polynom(sum)
    S = odd(S)
    if type(A) == Polynom:
        return S
    else:
        return odd(sum)


def summod(A, B):
    if type(A) == Polynom:
        a = A.coef
        b = B.coef
    else:
        a = A
        b = B
    k = max(a.shape[0], b.shape[0])
    if a.shape[0] < k:
        c = np.zeros(k)
        c[k - a.shape[0]:] = a
        a = c
    if b.shape[0] < k:
        c = np.zeros(k)
        c[k - b.shape[0]:] = b
        b = c
    sum = np.ones(k)
    for i in range(k):
        if a[i] == b[i]:
            sum[i] = 0
    S = Polynom(sum)
    S = odd(S)
    if type(A) == Polynom:
        return S
    else:
        return odd(sum)


def Mul(A, B):
    if type(A) == Polynom:
        a = A.coef.copy()
    else:
        a = A
    if type(B) == Polynom:
        b = B.coef
    else:
        b = B
    if a.shape[0] < b.shape[0]:
        a, b = b, a
    k = a.shape[0] + b.shape[0] - 1
    c = np.zeros(k)
    for i in range(0, b.shape[0]):
        s = np.zeros(k)
        if b[i] == 1:
            s[i:a.shape[0] + i] = a
        c = sum_pol(c, s)
    if type(A) == Polynom:
        return odd(Polynom(c))
    else:
        return odd(c)


def mod(A, B):
    if type(A) == Polynom:
        a = A.coef
    else:
        a = A
    if type(B) == Polynom:
        b = B.coef
    else:
        b = B
    # k = b.shape[0]
    if a.shape[0] < b.shape[0]:
        return Polynom(a)
    else:
        while a.shape[0] >= b.shape[0]:
            # c = np.zeros(k)
            # c[k - a.shape[0] - 1:] = a
            a = odd(summod(a, b))
    return Polynom(a)


def to_two(n):
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    if b == '':
        return np.array([0])
    else:
        t = np.zeros(len(b))
        for i in range(len(b)):
            t[i] = int(b[i])
        return t


def poww(A, k):
    if type(A) == Polynom:
        sol = A.coef
    else:
        sol = A
    if k == 0:
        sol = np.array([1.])
    else:
        for i in range(k - 1):
            sol = Mul(sol, A)
            sol = odd(sol)
    if type(sol) == Polynom:
        return sol
    else:
        return sol


def powgf2(A, k, P):
    a = A.coef
    d = to_two(k)
    b = np.array([1.])
    if k == 0:
        return np.array([1.])
    else:
        for i in range(d.shape[0]):
            b = Mul(poww(b, 2), poww(a, int(d[i])))
            b = mod(b, P)
        return b


def Trace(P, a):
    m2 = Polynom([0])
    for i in range(0, P.coef.shape[0] - 1):
        m1 = powgf2(a, 2 ** i, P)
        m2 = mod(sum_pol(m2, m1), P)
    return m2


def FormulaGM(P, alpha, i):
    lambd = Polynom([0, 1])
    F = mod(Mul(alpha, powgf2(lambd, i, P)), P)
    F = Trace(P, F)
    return F


def Lrp(p, L1):
    P = str_pol(p)
    p = ToStr(P)
    k = (P.coef.shape[0] - 1)
    d = 2 ** k - 1

    for i in range(0, d):
        g1 = 0
        for j in range(0, k):
            g = (int(L1[i + j]) * int(p[j])) % 2
            g1 = (g1 + g) % 2
        L1 += str(g1)

    L = str()
    alpha = Polynom([0, 1, 0, 0, 1])

    for i in range(0, int(2 ** (int(len(p))))):
        F = FormulaGM(P, alpha, i)
        L = L + ToStr(F)
    L2 = str()
    alpha = Polynom([0, 1])
    while L2.find(L1) != 0:
        L2 = str()
        lamb = Polynom([0, 1])
        for i in range(0, int(2 ** (int(len(p))))):
            F = FormulaGM(P, alpha, i)
            L2 = L2 + ToStr(F)
        alpha = mod(Mul(alpha, lamb), P)
    alpha = ToStr(alpha)
    return k, d, L1, L2, alpha, L.find(L2) + 1
