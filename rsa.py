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

# can confirm by decrypting encryption.

# primes


p = 1021
q = 107


# public key
n = p*q
e = 19


# mod
a = (p-1)*(q-1)

# private key
# d = e^-1 mod a

d = find(1, e, -1, a)
# message
#m = 152015

c = 36420

# encipher

#c = find(1, m, e, n)
#c = 35

# decipher

m = find(1, c, d, n)


# print

print(m)

print(d)
print(e)

# confidentiality: find c
# integrity: find m


# NOTES

# for double encryption to ensure both authenticity and confidentiality,

# alice wants to send bob message m
# alice will first encrypt with her private key d_alice
# then encrypt with bobs public key e_bob

# {{m}d_alice }e_bob

# Bob wants to receive alice's double encrypted message
# Bob first decrypts the first layer with d_bob
# Bob then decrypts the second layer with e_alice

# e_alice(d_bob(c))


# both conf and integrity
