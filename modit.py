def find(a, b, c, d):
    if (c < 0):
        x = modinv(b, d)
        c = c*-1
    else:
        x = b
    x = x**c % d
    a = a % d
    ans = (a * x) % d
    return ans


def gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = gcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = gcd(a, m)
    if g != 1:
        print("error, dont use this answer")
        return 0
    else:
        return x % m

# a*b^c mod d


a = 923
b = 15653
c = -3632
d = 262643
print(find(a, b, c, d))
