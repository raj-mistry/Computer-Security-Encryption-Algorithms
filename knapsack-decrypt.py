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


def reverseString(x):
    return x[::-1]


priv_k = [2, 3, 6, 13, 27, 52]
M = [62, 93, 81, 88, 102, 37]
n = 31
m = 105

encryptedmessage = 333

x = find(1, 31, -1, 105)

decrypt = find(encryptedmessage, x, 1, 105)

print(decrypt)

# now finding plain text
plaintext = ""

d = decrypt
for j in range(0, len(priv_k)):
    num = priv_k[len(priv_k)-j-1]
    if (num <= d):
        d = d-num
        plaintext = plaintext + "1"
    else:
        plaintext = plaintext + "0"
plaintext = reverseString(plaintext)


print(plaintext)
