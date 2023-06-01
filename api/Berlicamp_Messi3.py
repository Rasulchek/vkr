import numpy as np
from numpy.polynomial import Polynomial as Polynom


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
        if a[j] != 0:
            b = a[:j + 1]
            break
        else:
            b = np.array([0])
    if type(A) == Polynom:
        return Polynom(b)
    else:
        return b


def AddGF3(A, B):
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
    sum = np.zeros(k)
    for i in range(k):
        sum[i] = (a[i] + b[i]) % 3
    S = Polynom(sum)
    S = odd(S)
    if type(A) == Polynom:
        return S
    else:
        return odd(sum)


def SubGF3(A, B):
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
    for i in range(k):
        if (b[i] != 0):
            b[i] = 3 - b[i]
    sum = np.zeros(k)
    for i in range(k):
        sum[i] = (a[i] + b[i]) % 3
    S = Polynom(sum)
    S = odd(S)
    if type(A) == Polynom:
        return S
    else:
        return odd(sum)


def Mul3(A, B):
    if type(A) == Polynom:
        a = A.coef.copy()
    else:
        a = A
    if type(B) == Polynom:
        b = B.coef
    else:
        b = B
    if a.shape[0] <= b.shape[0]:
        a, b = b, a
    k = a.shape[0] + b.shape[0] + 1
    c = np.zeros(k)
    for i in range(0, b.shape[0]):
        s = np.zeros(k)
        if b[i] != 0:
            s[i:a.shape[0] + i] = a * b[i] % 3
        c = AddGF3(c, s)
    if type(A) == Polynom:
        return odd(Polynom(c))
    else:
        return odd(c)


def InverseInFp(b, p):
    c = b.coef
    for i in range(c.shape[0]):
        while c[i] > p:
            c[i] = c[i] - p
    return Polynom(c)


def pol_to_latex(pol):
    c = pol.coef
    la = str()
    if c[0] != 0:
        la += str(round(c[0])) + "+"
    if c.shape[0] > 1:
        if c[1] != 0:
            if c[1] != 1:
                la += str(round(c[1])) + "X" + "+"
            else:
                la += "X" + "+"
        for i in range(2, c.shape[0]):
            if c[i] != 0:
                if c[i] != 1:
                    la += str(round(c[i])) + "X^" + "{" + str(i) + "}"
                else:
                    la += "X^" + "{" + str(i) + "}"
                if i < c.shape[0] - 1:
                    la += "+"
    if la[len(la) - 1] == "+":
        la = la[:-1]
    return la


def Berlicamp_Messi3(lp):
    G = str_pol(lp)
    l = G.coef.shape[0]
    k = l // 2
    p = 3

    g = Polynom([1])
    h = Polynom([0, 1])
    m = 0
    b = Polynom([0])

    g_list = []
    h_list = []
    m_list = []
    b_list = []

    g_list.append(pol_to_latex(g))
    h_list.append(pol_to_latex(h))
    m_list.append(str(m))
    b_list.append(ToStr(b))

    g1 = g.copy()
    h1 = h.copy()

    L = []

    for j in range(1, l + 1):
        g1 = Mul3(b, h)
        g1 = SubGF3(g, g1)
        if not b.coef[0] == 0.0 and not m < 0:
            c = InverseInFp(b, p)
            h1 = Mul3(Polynom([0, 1]), g)
            h1 = Mul3(c, h1)
            m = 0 - m
        else:
            h1 = Mul3(Polynom([0, 1]), h)
            m = m + 1
        g = g1.copy()
        h = h1.copy()
        P = Mul3(g, G)
        b = Polynom([P.coef[j]])
        g_list.append(pol_to_latex(g))
        h_list.append(pol_to_latex(h))
        m_list.append(str(m))
        b_list.append(ToStr(b))
    h = ToStr(g)
    l_h = len(h)
    for i in range(0, l_h):
        L.insert(0, int(h[i]))
    r = int(k + 0.5 - m * 0.4)
    deg = len(ToStr(g)) - 1
    for i in range(0, r - deg):
        L.insert(0, 0)
    LL = str()
    for i in range(len(L)):
        LL += (str(int(L[i])))
    return l, k, g_list, h_list, m_list, b_list, LL
