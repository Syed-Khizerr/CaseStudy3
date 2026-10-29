#To implement the diffie hellman key exchange algorithm
p = 23
g = 5
a = 6
b = 15
A = pow(g,a,p)
B = pow(g,b,p)
shared_secret_a = pow(B,a,p)
shared_secret_b = pow(A,b,p)

print("Public Key A:", A)
print("Public Key B:", B)
print("Shared Secret Key (from A's perspective):", shared_secret_a)
print("Shared Secret Key (from B's perspective):", shared_secret_b)