'''
# Das Ziel des Programms: Verify an ECDSA-signature
# Date: 5.Juli 2020
# Die Sprache des Programms: Python
'''
import hashlib as hashlib   # used for hashing
import linecache as linecache
import re as re

# function used for finding inverse modulus
# This is not written by me, the source for this function:
# Source link: https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
########################################################################################################################
# Step 1: Input stage
sig_file = 'path\\to\\sig_file.txt'     # this has all the parameters required 
                                        # (run sign generation program to generate this file)
fptr_sig_file = open(sig_file, "r")

msg = linecache.getline(sig_file, 1)
msg = re.sub('(msg:)', '', msg)
msg = msg.strip()
print("Message is:", msg)

r_int = linecache.getline(sig_file, 3)
r_int = re.sub('(r:)', '', r_int)
r_int = int(r_int)
print("r:", r_int)

s_int = linecache.getline(sig_file, 5)
s_int = re.sub('(s:)', '', s_int)
s_int = int(s_int)
print("s:", s_int)

p_int = linecache.getline(sig_file, 7)
p_int = re.sub('(p in int:)', '', p_int)
p_int = int(p_int)
print("p (int):", p_int)

D_T_x = linecache.getline(sig_file, 9)
D_T_x = re.sub('(Public Key D_T x:)', '', D_T_x)
D_T_x = int(D_T_x)
print("D_T x (int):", D_T_x)

D_T_y = linecache.getline(sig_file, 11)
D_T_y = re.sub('(Public Key D_T y:)', '', D_T_y)
D_T_y = int(D_T_y)
print("D_T y (int):", D_T_y)

g_x = linecache.getline(sig_file, 13)
g_x = re.sub('(G x:)', '', g_x)
g_x = int(g_x)
print("G x (int):", g_x)

g_y = linecache.getline(sig_file, 15)
g_y = re.sub('(G y:)', '', g_y)
g_y = int(g_y)
print("G y (int):", g_y)

hash_func = linecache.getline(sig_file, 17)
hash_func = re.sub('(Hash function:)', '', hash_func)
print("Hash function used:", hash_func)

fptr_sig_file.close()
########################################################################################################################
# Step 2: Verification of the signature
# Step 2.1: Check r mod p and s mod p (1st check for verification)
if (r_int % p_int == 0) or (s_int % p_int == 0):
    print("Check 1 failed. Signature is invalid")
else:
    print("Check 1 passed. Moving on...")

# Step 2.2: Hash the message
h = hashlib.new('ripemd160')
h.update(msg.encode('utf-8'))
h_hex = h.hexdigest()
h_int = int(h_hex, 16)
print("Hashed message is:", h_hex)

# Step 2.3: Compute s_star where s_star * s = 1 mod p
s_star_int = modinv(s_int, p_int)

# Step 2.4: Compute L (x_l, y_l) where L = s_star * (h*G + r*D_T)
l_x_int = (s_star_int * ((h_int * g_x) + (r_int * D_T_x)))
l_y_int = (s_star_int * ((h_int * g_y) + (r_int * D_T_y)))
print("L x:", l_x_int)
print("L y:", l_y_int)
print("res:", l_x_int % p_int)

# Step 2.5: Final check for validity
if (l_x_int % p_int == r_int):
    print("Check 2 passed. Signature valid!")
else:
    print("Check 2 failed. Signature invalid")

