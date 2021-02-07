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
m = 152015

# public key (p,g,y)


p = 262643
g = 9563
d = 3632  # kpriv

# y=g^kpriv mod p
y = find(1, g, d, p)

# encipher
# random k relatively prime to p-1, used to encipher
k = 601
a = find(1, g, k, p)

# m = (da +kb) mod (p-1)
# use wolfram alpha to find b

b = 225835

# validate digital signature
# check if (y^a)*(a^b) mod p = g^m mod p

one = find(y**a * a**b, 1, 1, p)
two = find(1, g, m, p)

print(one == two)

# print

print(y)

print(one)
print(two)
