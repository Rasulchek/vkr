import math

bin_key = str('')
encr_str = str('')

def string_to_ascii_bin(string):
    enc = str('')
    for char in string:
        ascii_value = ord(char)
        bin_char = bin(ascii_value)[2:]
        enc = enc + bin_char.zfill(8)
    return enc


def bwcomplement(A):
    Ac = ''
    for i in range(0, 32):
        Ac = Ac + str((int(A[i]) + 1) % 2)
    return Ac


def bwandorexor(o, A, B):
    res = ''
    for i in range(0, 32):
        if o == 'And':
            res = res + str(int(A[i]) * int(B[i]))
        elif o == 'Or':
            res = res + str(((int(A[i]) + int(B[i]) + int(A[i]) * int(B[i])) % 2))
        elif o == 'Exor':
            res = res + str((int(A[i]) + int(B[i])) % 2)
    return res


def leftrotating(A, s):
    res = A[s:32] + A[0:s]
    return res


def rightrotating(A, s):
    res = A[32 - s:32] + A[0:32 - s]
    return res


# def summamod32(A, B):
#     res = ''
#     curry = 0
#     for i in range(0, 32):
#         cursum = (curry + int(A[31 - i]) + int(B[31 - i])) % 2
#         car = curry * int(A[31 - i]) + curry * int(B[31 - i]) + int(A[31 - i]) * int(A[31 - i])
#         if car >= 1:
#             curry = 1
#         else:
#             curry = 0
#         res = str(cursum) + res
#     return res

def summamod32(A, B):
    A = int(A, 2)
    B = int(B, 2)
    res = to_bin_32((A + B) % 2 ** 32)
    return res


def to_bin_32(number):
    binary = bin(number)[2:]  # Преобразование в двоичную строку и удаление префикса '0b'
    padded_binary = binary.zfill(32)
    return padded_binary


def bin_16(bin):
    x = hex(int(bin, 2))[2:]
    x8 = x.zfill(8)
    return x8.upper()


def bin_10(bin):
    return int(bin, 2)


def f1(b, c, d):
    bc = bwandorexor('And', b, c)
    b_ = bwcomplement(b)
    b_d = bwandorexor('And', b_, d)
    res = bwandorexor('Or', bc, b_d)
    return res


def g1(b, c, d):
    bc = bwandorexor('And', b, c)
    bd = bwandorexor('And', b, d)
    cd = bwandorexor('And', c, d)
    bcbd = bwandorexor('Or', bc, bd)
    res = bwandorexor('Or', bcbd, cd)
    return res


def h1(b, c, d):
    bc = bwandorexor('Exor', b, c)
    res = bwandorexor('Exor', bc, d)
    return res


def gamma(a, i):
    y1 = 0x5A827999
    y2 = 0x6ED9EBA1
    y3 = 0x8F1BBCDC
    y4 = 0xCA62C1D6
    y1 = to_bin_32(y1)
    y2 = to_bin_32(y2)
    y3 = to_bin_32(y3)
    y4 = to_bin_32(y4)
    x = []
    x.append(to_bin_32(i))
    for j in range(1, 16):
        x.append(to_bin_32(0))
    for j in range(16, 80):
        v1 = bwandorexor('Exor', x[j - 3], x[j - 8])
        v2 = bwandorexor('Exor', x[j - 14], x[j - 16])
        v3 = bwandorexor('Exor', v1, v2)
        res = leftrotating(v3, 1)
        x.append(res)
    H0 = a[0: 32]
    H1 = a[32: 64]
    H2 = a[64: 96]
    H3 = a[96: 128]
    H4 = a[128: 160]

    A = a[0: 32]
    B = a[32: 64]
    C = a[64: 96]
    D = a[96: 128]
    E = a[128: 160]
    for j in range(0, 20):
        A5 = leftrotating(A, 5)
        fbcd = f1(B, C, D)
        t1 = summamod32(A5, fbcd)
        t2 = summamod32(E, x[j])
        t3 = summamod32(t1, t2)
        t = summamod32(t3, y1)
        A = t
        B = A
        C = leftrotating(B, 30)
        D = C
        E = D
    for j in range(20, 40):
        A5 = leftrotating(A, 5)
        hbcd = h1(B, C, D)
        t1 = summamod32(A5, hbcd)
        t2 = summamod32(E, x[j])
        t3 = summamod32(t1, t2)
        t = summamod32(t3, y2)
        A = t
        B = A
        C = leftrotating(B, 30)
        D = C
        E = D
    for j in range(40, 60):
        A5 = leftrotating(A, 5)
        gbcd = g1(B, C, D)
        t1 = summamod32(A5, gbcd)
        t2 = summamod32(E, x[j])
        t3 = summamod32(t1, t2)
        t = summamod32(t3, y3)
        A = t
        B = A
        C = leftrotating(B, 30)
        D = C
        E = D
    for j in range(60, 80):
        A5 = leftrotating(A, 5)
        hbcd1 = h1(B, C, D)
        t1 = summamod32(A5, hbcd1)
        t2 = summamod32(E, x[j])
        t3 = summamod32(t1, t2)
        t = summamod32(t3, y4)
        A = t
        B = A
        C = leftrotating(B, 30)
        D = C
        E = D
    H0 = summamod32(H0, A)
    H1 = summamod32(H1, B)
    H2 = summamod32(H2, C)
    H3 = summamod32(H3, D)
    H4 = summamod32(H4, E)
    return H0, H1, H2, H3, H4

def Fa(a, i):
    H = gamma(a, math.floor(i/5))
    return H[i % 5]


def Initialize(n, l, R, T):
    A = bwandorexor('Exor', n, R[4*l])
    n8 = rightrotating(n, 8)
    B = bwandorexor('Exor', n8, R[4*l+1])
    n16 = rightrotating(n, 16)
    C = bwandorexor('Exor', n16, R[4*l+2])
    n24 = rightrotating(n, 24)
    D = bwandorexor('Exor', n24, R[4*l+3])
    for j in range(1, 3):
        P = bwandorexor('And', A, to_bin_32(0x000007FC))
        B = summamod32(B, T[math.floor(bin_10(P)/4)])
        A = rightrotating(A, 9)

        P = bwandorexor('And', B, to_bin_32(0x000007FC))
        C = summamod32(C, T[math.floor(bin_10(P)/4)])
        B = rightrotating(B, 9)

        P = bwandorexor('And', C, to_bin_32(0x000007FC))
        D = summamod32(D, T[math.floor(bin_10(P)/4)])
        C = rightrotating(C, 9)

        P = bwandorexor('And', D, to_bin_32(0x000007FC))
        A = summamod32(A, T[math.floor(bin_10(P)/4)])
        D = rightrotating(D, 9)

    n1 = D
    n2 = B
    n3 = A
    n4 = C

    P = bwandorexor('And', A, to_bin_32(0x000007FC))
    B = summamod32(B, T[math.floor(bin_10(P)/4)])
    A = rightrotating(A, 9)

    P = bwandorexor('And', B, to_bin_32(0x000007FC))
    C = summamod32(C, T[math.floor(bin_10(P)/4)])
    B = rightrotating(B, 9)

    P = bwandorexor('And', C, to_bin_32(0x000007FC))
    D = summamod32(D, T[math.floor(bin_10(P)/4)])
    C = rightrotating(C, 9)

    P = bwandorexor('And', D, to_bin_32(0x000007FC))
    A = summamod32(A, T[math.floor(bin_10(P)/4)])
    D = rightrotating(D, 9)
    return A, B, C, D, n1, n2, n3, n4


def SEAL(a, n):
    n = to_bin_32(n)
    T = []
    S = []
    R = []
    for i in range(0, 512):
        T.append(Fa(a, i))
    for j in range(0, 256):
        S.append(Fa(a, 0x00001000+j))
    for k in range(0, 16):
        R.append(Fa(a, 0x00002000+k))

    l = 0
    y = str('')
    while len(y) < 8192:
        A, B, C, D, n1, n2, n3, n4 = Initialize(n, l, R, T)
        for i in range (1, 65):
            P = bwandorexor('And', A, to_bin_32(0x000007FC))
            B = summamod32(B, T[math.floor(bin_10(P)/4)])
            A = rightrotating(A, 9)
            B = bwandorexor('Exor', B, A)

            Q = bwandorexor('And', B, to_bin_32(0x000007FC))
            C = bwandorexor('Exor', C, T[math.floor(bin_10(Q)/4)])
            B = rightrotating(B, 9)
            C = summamod32(C, B)

            PC = summamod32(P, C)
            P = bwandorexor('And', PC, to_bin_32(0x000007FC))
            D = summamod32(D, T[math.floor(bin_10(P)/4)])
            C = rightrotating(C, 9)
            D = bwandorexor('Exor', D, C)

            QD = summamod32(Q, D)
            Q = bwandorexor('And', QD, to_bin_32(0x000007FC))
            A = bwandorexor('Exor', A, T[math.floor(bin_10(Q)/4)])
            D = rightrotating(D, 9)
            A = summamod32(A, D)

            PA = summamod32(P, A)
            P = bwandorexor('And', PA, to_bin_32(0x000007FC))
            B = bwandorexor('Exor', B, T[math.floor(bin_10(P)/4)])
            A = rightrotating(A, 9)

            QB = summamod32(Q, B)
            Q = bwandorexor('And', QB, to_bin_32(0x000007FC))
            C = summamod32(C, T[math.floor(bin_10(Q)/4)])
            B = rightrotating(B, 9)

            PC = summamod32(P, C)
            P = bwandorexor('And', PC, to_bin_32(0x000007FC))
            D = bwandorexor('Exor', D, T[math.floor(bin_10(P)/4)])
            C = rightrotating(C, 9)

            QD = summamod32(Q, D)
            Q = bwandorexor('And', QD, to_bin_32(0x000007FC))
            A = summamod32(A, T[math.floor(bin_10(Q)/4)])
            D = rightrotating(D, 9)

            y1 = summamod32(B, S[4*i - 4])
            y2 = bwandorexor('Exor', C, S[4*i-3])
            y3 = summamod32(D, S[4*i - 2])
            y4 = bwandorexor('Exor', A, S[4*i-1])

            global bin_key
            bin_key = bin_key + y1 + y2 + y3 + y4

            y1 = bin_16(y1)
            y2 = bin_16(y2)
            y3 = bin_16(y3)
            y4 = bin_16(y4)

            y = y + y1 + y2 + y3 + y4
            if len(y) > 8192:
                return y, T, S, R
            if i % 2 == 0:
                A = summamod32(A, n1)
                C = summamod32(C, n2)
            else:
                A = summamod32(A, n3)
                C = summamod32(C, n4)
        l = l + 1
    T16 = []
    for i in range(0, len(T)):
        T16.append(bin_16(T[i]))
    S16 = []
    for i in range(0, len(S)):
        S16.append(bin_16(S[i]))
    R16 = []
    for i in range(0, len(R)):
        R16.append(bin_16(R[i]))
    return y, T16, S16, R16


def encrypt(string):
    bin_str = string_to_ascii_bin(string)
    res = str('')
    res16 = str('')

    for i in range(0, len(bin_str)):
        res = res + str((int(bin_str[i]) + int(bin_key[i])) % 2)

    for i in range(0, len(res), 4):
        res16 += hex(int(res[i: i + 4], 2))[2:]
    str16 = hex(int(bin_str, 2))[2:]
    return str16.upper(), res16.upper()


def decrypt(cr):
    res = str('')
    decr = str('')
    cript = str('')
    for i in range(0, len(cr)):
        cript += bin(int(cr[i], 16))[2:].zfill(4)

    for i in range(0, len(cript)):
        res = res + str((int(cript[i]) + int(bin_key[i])) % 2)

    res16 = hex(int(res, 2))[2:]
    for i in range(0, len(res), 8):
        ch = chr(int(res[i: i+8], 2))
        decr = decr + ch
    return decr, res16.upper()
