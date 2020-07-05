'''
# Das Ziel des Programms: Create an ECDSA-signature
# Date: 5.Juli 2020
# Die Sprache des Programms: Python
'''
import hashlib as hashlib   # used for hashing
import linecache as linecache
import secrets as secrets   # used for CS-PRNG

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
out_file = 'path\\to\\out_file.txt' # this where the output will be stored
txt_file = 'path\\to\\ecdsa_file.txt'   # this where the input parameters are stored
sig_file = 'path\\to\\sig_file.txt'     # this will be used for verification program 

fptr_sig_file = open(sig_file, "w")

fptr_out_file = open(out_file, "w")
fptr_out_file.write("Elliptic curve parameters are:\n\n")

curve_id = linecache.getline(txt_file, 1) # get the curve field and equation used
fptr_out_file.write("Curve type: ")
fptr_out_file.write(curve_id)
fptr_out_file.write("\n")

p_hex = linecache.getline(txt_file, 2) # get p: huge prime number
fptr_out_file.write("Huge prime number p (hex): ")
fptr_out_file.write(p_hex)
fptr_out_file.write("\n")

p_int = int(p_hex, 16)
fptr_out_file.write("Huge prime number p (int): ")
fptr_out_file.write(str(p_int))
fptr_out_file.write("\n")

A_hex = linecache.getline(txt_file, 3) # get A:
fptr_out_file.write("EC parameter A (hex): ")
fptr_out_file.write(A_hex)
fptr_out_file.write("\n")

A_int = int(A_hex, 16)
fptr_out_file.write("EC parameter A (int): ")
fptr_out_file.write(str(A_int))
fptr_out_file.write("\n")

B_hex = linecache.getline(txt_file, 4) # get B:
fptr_out_file.write("EC parameter B (hex): ")
fptr_out_file.write(B_hex)
fptr_out_file.write("\n")

B_int = int(B_hex, 16)
fptr_out_file.write("EC parameter B (int): ")
fptr_out_file.write(str(B_int))
fptr_out_file.write("\n")

x_hex = linecache.getline(txt_file, 5) # get x(P_0): Gx -> a point in E
fptr_out_file.write("Generator point x (hex): ")
fptr_out_file.write(x_hex)
fptr_out_file.write("\n")

x_int = int(x_hex, 16)
fptr_out_file.write("Generator point x (int): ")
fptr_out_file.write(str(x_int))
fptr_out_file.write("\n")

y_hex = linecache.getline(txt_file, 6) # get y(P_0): Gy -> a point in E
fptr_out_file.write("Generator point y (hex): ")
fptr_out_file.write(y_hex)
fptr_out_file.write("\n")

y_int = int(y_hex, 16)
fptr_out_file.write("Generator point y (int): ")
fptr_out_file.write(str(y_int))
fptr_out_file.write("\n")

q_hex = linecache.getline(txt_file, 7) # get q: huge good prime divisor
fptr_out_file.write("Huge prime, good divisor q (hex): ")
fptr_out_file.write(q_hex)
fptr_out_file.write("\n")

q_int = int(q_hex, 16)
fptr_out_file.write("Huge prime, good divisor q (int): ")
fptr_out_file.write(str(q_int))
fptr_out_file.write("\n")

hash_func = linecache.getline(txt_file, 8)  # get the hash function type
fptr_out_file.write("Hash function to be used: ")
fptr_out_file.write(hash_func)
fptr_out_file.write("---------------------------------------------------------------------------------------------\n\n")
########################################################################################################################
# Step 2: Setup for each participant T a pair (d_T, D_T)
# Step 2.1: Compute d_T (Private Key)
d_T = secrets.randbelow(p_int-1)    # generate a random number between 1 and p-1
fptr_out_file.write("Private Key: ")
fptr_out_file.write(str(d_T))
fptr_out_file.write("\n\n")

# Step 2.2: Compute D_T (Public Key)
D_T_x = d_T * x_int
D_T_y = d_T * y_int
fptr_out_file.write("Public Key D_T_x: ")
fptr_out_file.write(str(D_T_x))
fptr_out_file.write("\n\n")
fptr_out_file.write("Public Key D_T_y: ")
fptr_out_file.write(str(D_T_y))
fptr_out_file.write("\n\n")
########################################################################################################################
# Step 3: Signing where the participant T wants to sign the message m
# Step 3.1: Compute the Hash value of the message m
msg = input("Input the message:")
fptr_out_file.write("Message to be hashed: ")
fptr_out_file.write(msg)
fptr_out_file.write("\n\n")

h = hashlib.new('ripemd160')
h.update(msg.encode('utf-8'))
h_hex = h.hexdigest()
fptr_out_file.write("Hex Hash value(RIPEMD-160) of the message: ")
fptr_out_file.write(h_hex)
fptr_out_file.write("\n\n")

h_int = int(h_hex, 16)
fptr_out_file.write("int Hash value(RIPEMD-160) of the message: ")
fptr_out_file.write(str(h_int))
fptr_out_file.write("\n\n")

# Step 3.2: Generate random value k where 1<=k<=p
while(1):
    k_int = secrets.randbelow(p_int)    # generate a random number between 1 and p
    fptr_out_file.write("Random value k is: ")
    fptr_out_file.write(str(k_int))
    fptr_out_file.write("\n\n")

    # Step 3.3: Generate K = [k]*G = (x_k, y_k)
    x_k_int = k_int * x_int
    y_k_int = k_int * y_int
    fptr_out_file.write("K (x_k): ")
    fptr_out_file.write(str(x_k_int))
    fptr_out_file.write("\n\n")
    fptr_out_file.write("K (y_k): ")
    fptr_out_file.write(str(y_k_int))
    fptr_out_file.write("\n\n")

    # Step 3.4: Check if r = x_k mod p == 0 If yes, go to step 3.2
    if ((x_k_int % p_int) != 0):
        r_int = x_k_int % p_int
        fptr_out_file.write("R: ")
        fptr_out_file.write(str(r_int))
        fptr_out_file.write("\n\n")

        # Step 3.5: Compute k_star where k * k_star = 1 mod p
        k_star_int = modinv(k_int, p_int)
        fptr_out_file.write("k_star: ")
        fptr_out_file.write(str(k_star_int))
        fptr_out_file.write("\n\n")

        # Step 3.6: Check if s = k_star * (h + r*d_T) mod p == 0
        s_int = k_star_int * (h_int + (r_int * d_T))
        if (s_int % p_int != 0):
            s_int = s_int % p_int
            fptr_out_file.write("s: ")
            fptr_out_file.write(str(s_int))
            fptr_out_file.write("\n\n")
            break
        else:
            continue
    else:
        continue

print("Digital signature for message:", msg, "is (r, s): (", r_int, ",", s_int, ")")

fptr_out_file.close()

# This file is to be used for signature verification program
fptr_sig_file.write("msg: ")
fptr_sig_file.write(msg)
fptr_sig_file.write("\n\n")

fptr_sig_file.write("r: ")
fptr_sig_file.write(str(r_int))
fptr_sig_file.write("\n\n")

fptr_sig_file.write("s: ")
fptr_sig_file.write(str(s_int))
fptr_sig_file.write("\n\n")

fptr_sig_file.write("p in int: ")
fptr_sig_file.write(str(p_int))
fptr_sig_file.write("\n\n")

fptr_sig_file.write("Public Key D_T x: ")
fptr_sig_file.write(str(D_T_x))
fptr_sig_file.write("\n\n")

fptr_sig_file.write("Public Key D_T y: ")
fptr_sig_file.write(str(D_T_y))
fptr_sig_file.write("\n\n")

fptr_sig_file.write("G x: ")
fptr_sig_file.write(str(x_int))
fptr_sig_file.write("\n\n")

fptr_sig_file.write("G y: ")
fptr_sig_file.write(str(y_int))
fptr_sig_file.write("\n\n")

fptr_sig_file.write("Hash function: ")
fptr_sig_file.write(hash_func)
fptr_sig_file.write("\n\n")

fptr_sig_file.close()