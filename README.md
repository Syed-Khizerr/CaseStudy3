1) RSA

import math 
p=int(input("enter prime:"))
q=int(input("enter prime:"))
n=p*q 
phi=(p-1)*(q-1) 
for e in range(2, phi):
    if math.gcd(e, phi)==1:
        break
for d in range(2, phi):
    if (e*d)%phi==1:
        break
print("Pubic key:", (e, n))
print("Private key:", (d, n))
m=int(input("Enter message(number): "))
c=pow(m,e,n)
print("Encrypted message:", c)
decrypted=pow(c,d,n) 
print("Decrypted message:", decrypted)

--------------------------------------------------------------------------------------------------------------------------------------------
2) DES

pip install pycryptodome

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
key = b"12345678"
cipher = DES.new(key, DES.MODE_ECB)
plaintext = input("Enter Plaintext: ")
encrypted = cipher.encrypt(pad(plaintext.encode(), 8))
print("Encrypted (Hex):", encrypted.hex())
decrypted = unpad(cipher.decrypt(encrypted), 8)
print("Decrypted Text:", decrypted.decode())

------------------------------------------------------------------------------------------------------------------------------------------
3) AES

from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad, unpad 
key=b"1234567890123456"
cipher=AES.new(key, AES.MODE_ECB)
plaintext=input("Enter text: ")
encrypted=cipher.encrypt(pad(plaintext.encode(), AES.block_size))
print("Encrypted text:", encrypted.hex())
decipher=AES.new(key, AES.MODE_ECB)
decrypted=unpad(decipher.decrypt(encrypted), AES.block_size)
print("Decrpted Text:", decrypted.decode()) 

------------------------------------------------------------------------------------------------------------------------------------------
4) CEASAR CIPHER

text = input("Enter text: ")
k = int(input("Enter key: "))
encrypted = ""
for ch in text:
    if ch.isalpha():
        encrypted += chr((ord(ch.upper()) - 65 + k) % 26 + 65)
    else:
        encrypted += ch
print("Encrypted:", encrypted)
decrypted = ""
for ch in encrypted:
    if ch.isalpha():
        decrypted += chr((ord(ch) - 65 - k) % 26 + 65)
    else:
        decrypted += ch
print("Decrypted:", decrypted)

------------------------------------------------------------------------------------------------------------------------------------------
5) PLAYFAIR CIPHER

key = input("Enter key: ").upper().replace("J", "I")
text = input("Enter plaintext: ").upper().replace("J", "I")
s = ""
for ch in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
    if ch not in s:
        s += ch
matrix = [s[i:i+5] for i in range(0, 25, 5)]
pairs = []
i = 0
while i < len(text):
    a = text[i]
    if i + 1 == len(text):
        pairs.append(a + "X")
        break
    b = text[i + 1]
    if a == b:
        pairs.append(a + "X")
        i += 1
    else:
        pairs.append(a + b)
        i += 2
cipher = ""
for a, b in pairs:
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == a:
                r1, c1 = r, c
            if matrix[r][c] == b:
                r2, c2 = r, c
    if r1 == r2:              
        cipher += matrix[r1][(c1 + 1) % 5]
        cipher += matrix[r2][(c2 + 1) % 5]
    elif c1 == c2:            
        cipher += matrix[(r1 + 1) % 5][c1]
        cipher += matrix[(r2 + 1) % 5][c2]
    else:                    
        cipher += matrix[r1][c2]
        cipher += matrix[r2][c1]
print("Encrypted:", cipher)

------------------------------------------------------------------------------------------------------------------------------------------
6) HILL CIPHER

text = input("Enter text: ").upper()
if len(text) % 3:
    text += "X" * (3 - len(text) % 3)
cipher = ""
for i in range(0, len(text), 3):
    a, b, c = [ord(x)-65 for x in text[i:i+3]]
    cipher += chr((6*a + 24*b + c) % 26 + 65)
    cipher += chr((13*a + 16*b + 10*c) % 26 + 65)
    cipher += chr((20*a + 17*b + 15*c) % 26 + 65)
print("Encrypted:", cipher)
plain = ""
for i in range(0, len(cipher), 3):
    a, b, c = [ord(x)-65 for x in cipher[i:i+3]]
    plain += chr((8*a + 5*b + 10*c) % 26 + 65)
    plain += chr((21*a + 8*b + 21*c) % 26 + 65)
    plain += chr((21*a + 12*b + 8*c) % 26 + 65)
print("Decrypted:", plain)

------------------------------------------------------------------------------------------------------------------------------------------
7) RAILFENCE

text = input("Enter plaintext: ").replace(" ", "")
depth = int(input("Enter depth: "))
rails = [""] * depth
row = 0
direction = 1
for ch in text:
    rails[row] += ch
    if row == 0:
        direction = 1
    elif row == depth - 1:
        direction = -1
    row += direction
cipher = "".join(rails)
print("Encrypted:", cipher)

------------------------------------------------------------------------------------------------------------------------------------------
8) ROW TRANSPOSITION

text = input("Enter plaintext: ").replace(" ", "").upper()
key = input("Enter key: ")
key = [int(x) for x in key]
cipher = ""
n = len(key)
for k in sorted(key):
    col = key.index(k)
    for i in range(col, len(text), n):
        cipher += text[i]
print("Encrypted:", cipher)
------------------------------------------------------------------------------------------------------------------------------------------
9) COLUMN TRANSPOSITION

text = input("Enter plaintext: ").replace(" ", "").lower()
key = input("Enter column order: ")
cols = len(key)
cipher = ""
for k in key:
    for i in range(int(k) - 1, len(text), cols):
        cipher += text[i]
print("Encrypted:", cipher)
------------------------------------------------------------------------------------------------------------------------------------------

#casaer cipher
k = int(input("Enter key: "))
ch = input("Enter e for encryption or d for decryption: ")
t = input("Enter text: ")
if ch == 'd':
    k = -k
r = ""
for c in t:
    if c.isalpha():
        b = ord('A') if c.isupper() else ord('a')
        r += chr((ord(c) - b + k) % 26 + b)
    else:
        r += c
print("Result:", r)


#Playfair
def matrix(key):
    s = ""
    for c in key.upper() + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c == "J": c = "I"
        if c not in s:
            s += c
    return [s[i:i+5] for i in range(0,25,5)]

def pos(m, c):
    for i in range(5):
        for j in range(5):
            if m[i][j] == c:
                return i,j

def playfair(text, key, dec=False):
    m = matrix(key)
    text = ''.join(c for c in text.upper() if c.isalpha()).replace("J","I")

    if not dec:
        p = []
        i = 0
        while i < len(text):
            a = text[i]
            b = text[i+1] if i+1 < len(text) else "X"
            if a == b:
                p.append(a+"X")
                i += 1
            else:
                p.append(a+b)
                i += 2
    else:
        p = [text[i:i+2] for i in range(0,len(text),2)]

    r = ""
    d = -1 if dec else 1

    for a,b in p:
        r1,c1 = pos(m,a)
        r2,c2 = pos(m,b)

        if r1 == r2:
            r += m[r1][(c1+d)%5] + m[r2][(c2+d)%5]
        elif c1 == c2:
            r += m[(r1+d)%5][c1] + m[(r2+d)%5][c2]
        else:
            r += m[r1][c2] + m[r2][c1]
    return r
key = input("Enter key: ")
text = input("Enter text: ")
ch = input("e/d: ")

print("Result:", playfair(text, key, ch == 'd'))




#Hill cipher
import numpy as np

K = np.array([[6,24,1],
              [13,16,10],
              [20,17,15]])

I = np.array([[8,5,10],
              [21,8,21],
              [21,12,8]])

ch = input("e/d: ")
t = input("Enter text: ").upper()

M = K if ch == 'e' else I

while len(t) % 3:
    t += 'X'

r = ""
for i in range(0, len(t), 3):
    p = np.array([ord(c)-65 for c in t[i:i+3]])
    c = np.dot(M, p) % 26
    r += ''.join(chr(x+65) for x in c)

print("Result:", r.rstrip('X') if ch == 'd' else r)



#Railfence
def encrypt(t, k):
    rail = [''] * k
    r, d = 0, 1

    for c in t:
        rail[r] += c
        if r == 0: d = 1
        elif r == k-1: d = -1
        r += d

    return ''.join(rail)

def decrypt(c, k):
    n = len(c)
    pattern = list(range(k)) + list(range(k-2,0,-1))
    rows = [pattern[i % len(pattern)] for i in range(n)]

    rail = []
    p = 0

    for r in range(k):
        cnt = rows.count(r)
        rail.append(list(c[p:p+cnt]))
        p += cnt

    return ''.join(rail[r].pop(0) for r in rows)

k = int(input("Enter rails: "))
t = input("Enter text: ")
c = encrypt(t,k)

print("Encrypted:", c)
print("Decrypted:", decrypt(c,k))


#row transformation
def encrypt(t, key):
    n = len(key)
    rows = [t[i:i+n] for i in range(0,len(t),n)]
    return ''.join(rows[i-1] for i in key)

def decrypt(c, key):
    n = len(key)
    size = len(c)//n
    rows = [''] * n
    p = 0

    for k in key:
        rows[k-1] = c[p:p+size]
        p += size

    return ''.join(rows)

key = list(map(int,input("Enter key order: ").split()))
t = input("Enter text: ")

c = encrypt(t,key)

print("Encrypted:",c)
print("Decrypted:",decrypt(c,key))


#columnar transformation
def encrypt(t, key):
    n = len(key)
    return ''.join(t[i-1::n] for i in key)

def decrypt(c, key):
    n = len(key)
    rows = len(c)//n
    cols = [''] * n
    p = 0

    for k in key:
        cols[k-1] = c[p:p+rows]
        p += rows

    return ''.join(cols[j][i] for i in range(rows) for j in range(n))

key = list(map(int,input("Enter key order: ").split()))
t = input("Enter text: ")

c = encrypt(t,key)

print("Encrypted:",c)
print("Decrypted:",decrypt(c,key))


#AES
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key=b"1234567890123456"
cipher=AES.new(key, AES.MODE_ECB)
plaintext=input("Enter text: ")

encrypted=cipher.encrypt(pad(plaintext.encode(), AES.block_size))
print("Encrypted text:", encrypted.hex())

decipher=AES.new(key, AES.MODE_ECB)
decrypted=unpad(decipher.decrypt(encrypted), AES.block_size)
print("Decrpted Text:", decrypted.decode())


#DES
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key=b"12345678"
cipher=DES.new(key, DES.MODE_ECB)
plaintext="Hello DES"

encrypted=cipher.encrypt(pad(plaintext.encode(), DES.block_size))
print("Encrypted text:", encrypted.hex())

decipher=DES.new(key, DES.MODE_ECB)
decypted=unpad(decipher.decrypt(encrypted), DES.block_size)
print("Decrpted Text:", decypted.decode())



#RSA
import math

p=7919
q=1009

n=p*q
phi=(p-1)*(q-1)

for e in range(2, phi):
    if math.gcd(e, phi)==1:
        break

for d in range(2, phi):
    if (e*d)%phi==1:
        break

print("Pubic key:", (e, n))
print("Private key:", (d, n))

m=int(input("Enter message(number): "))

c=pow(m,e,n)
print("Encrypted message:", c)
decrypted=pow(c,d,n)
print("Decrypted message:", decrypted)



#railfence
def encrypt(text, depth):
    text = text.replace(" ", "")
    rails = [""] * depth
    row = 0
    down = True

    for ch in text:
        rails[row] += ch

        if row == 0:
            down = True
        elif row == depth - 1:
            down = False

        row += 1 if down else -1

    return "".join(rails)


def decrypt(cipher, depth):
    n = len(cipher)

    pattern = [[""] * n for _ in range(depth)]
    row = 0
    down = True

    # Mark zigzag positions
    for col in range(n):
        pattern[row][col] = "*"

        if row == 0:
            down = True
        elif row == depth - 1:
            down = False

        row += 1 if down else -1

    # Fill marked positions with ciphertext
    index = 0
    for i in range(depth):
        for j in range(n):
            if pattern[i][j] == "*":
                pattern[i][j] = cipher[index]
                index += 1

    # Read in zigzag order
    result = ""
    row = 0
    down = True

    for col in range(n):
        result += pattern[row][col]

        if row == 0:
            down = True
        elif row == depth - 1:
            down = False

        row += 1 if down else -1

    return result


# Main Program
text = input("Enter Plain Text: ")
depth = int(input("Enter Depth: "))

encrypted = encrypt(text, depth)
decrypted = decrypt(encrypted, depth)

print("Encrypted Text:", encrypted)
print("Decrypted Text:", decrypted) 
