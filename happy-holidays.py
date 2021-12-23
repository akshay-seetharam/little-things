def heap_perm(n, A):
    if n == 1: yield A
    else:
        for i in range(n-1):
            for hp in heap_perm(n-1, A): yield hp
            j = 0 if (n % 2) == 1 else i
            A[j],A[n-1] = A[n-1],A[j]
        for hp in heap_perm(n-1, A): yield hp

def works(perm):
    h = perm[0]
    a = perm[1]
    p = perm[2]
    y = perm[3]
    o = perm[4]
    l = perm[5]
    i = perm[6]
    d = perm[7]
    s = perm[8]
    return abs(h * 1E+4 + a * 1E+3 + p * 1E+2 + p * 1E+1 + y * 1E+0 + h * 1E+7 + o * 1E+6 + l * 1E+5 + i * 1E+4 + d * 1E+3 + a * 1E+2 + y * 1E+1 + s * 1E+0 - 10101010 * h - 1010101 * o) == 0, [h, a, p, p, y], [h, o, l, i, d, a, y, s]

    

for i in heap_perm(10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
    yes, happy, holidays = works(i)
    if yes:
        print(happy, holidays)

