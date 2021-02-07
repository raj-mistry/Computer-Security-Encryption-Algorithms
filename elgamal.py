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


# message
m = 12404

# public key (p,g,y)


p = 262681
g = 1063
kpriv = 1039

# y=g^kpriv mod p
y = find(1, g, kpriv, p)

# encipher
# random k relatively prime to p-1, used to encipher
k = 29
c1 = find(1, g, k, p)
c2 = find(m, y, k, p)


# decipher

m = find(c2, c1, -1*kpriv, p)

# print

print(y)

print(c1)
print(c2)
print(m)
