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


publickey = [43, 40, 37, 28, 13, 69]
#privatekey = [2, 3, 6, 13, 27, 52]
n = 43
m = 89

x = find(1, n, -1, m)

# generating private key


privatekey = []
for i in range(0, len(publickey)):
    num = find(find(1, n, -1, m), publickey[i], 1, m)
    privatekey.append(num)

print(privatekey)

"""

# generating public key

publickey = []

for i in range(0, len(privatekey)):
    num = find(privatekey[i], n, 1, m)
    publickey.append(num)

print(publickey)

"""
