'''
# Das Ziel des Programms: RSA-AES Encryption Schema
# Date: 10.Juni 2020
# Die Sprache des Programms: Python
'''
import sys as sys
import re as re
import linecache as linecache
import sympy as sp
import math as math
'''
Steps to follow:
1. Input n
2. Get f1 and f2 where n = f1 * f2
3. Get phi_n The Euler Totient function where phi_n = (p-1) * (q-1)
4. Get Private Key d where e * d mod phi_n = 1
5. Get the key k where c^d mod n = k
6. Use k to decrypt the message 
'''
########################################################################################################################
# Step 1: Input the basic parameters
txt_file = "/Users/adityajayanti/Desktop/rsa_assignment/RSA_AES_cipher_k.txt"

# Step 1.1: Get the Public RSA Key n value (in int)
pub_rsa_key_n = linecache.getline(txt_file, 1)
pub_rsa_key_n = re.sub('[n=]', '', pub_rsa_key_n)   # remove "n=" from the text before storing in the string
pub_rsa_key_n = int(pub_rsa_key_n)
print("Public RSA Key (n): ", pub_rsa_key_n)

# Step 1.2: Get the Public RSA Key e value (in int)
pub_rsa_key_e = linecache.getline(txt_file, 3)
pub_rsa_key_e = re.sub('[e=]', '', pub_rsa_key_e)
pub_rsa_key_e = int(pub_rsa_key_e)
print("Public RSA Key (e): ", pub_rsa_key_e)

# Step 1.3: Get the Encrypted Session Key s value (in int)
enc_sess_key = linecache.getline(txt_file, 5)
enc_sess_key = re.sub('[s=]', '', enc_sess_key)
enc_sess_key = int(enc_sess_key)
print("Encrypted session key (s): ", enc_sess_key)

# Step 1.4: Get the Encrypted message c text (in Hex but stored as string)
cipher_msg = linecache.getline(txt_file, 7)
cipher_msg = re.sub('[c=]', '', cipher_msg)
print("Cipher text is: ", cipher_msg)
########################################################################################################################
# Step 2: Find the factors f1 and f2 (Prime factors of 'n')
f1, f2 = sp.ntheory.factorint(pub_rsa_key_n)    # returns the two factors
if (sp.isprime(f1) & sp.isprime(f2)):
    print("The two PRIME factors for the given 'n' are: ")
else:
    print("The two factors for the given 'n' are NOT PRIME. ")
print("Factor 1:", f1)
print("Factor 2:", f2)
########################################################################################################################
# Step 3: Find phi_n (Euler Totient function)
phi_n = (f1 - 1) * (f2 - 1)
print("Value of Phi(n) is:", phi_n)
########################################################################################################################
# Step 4: Find Private Key priv_key (using Extended Euclids Algorithm)
#   Here the program written in Julia is called.
#   The Julia program calculates the private key d
#   and stores the value d in j_code_out
#   This part of code was written in Julia because
#   Python was not able to handle big float values
print("Run the Julia program (finding_d_rsa.jl) to obtain the value of d")
d = int(input("Enter the value of d obtained from the Julia program: "))
########################################################################################################################
# Step 5: Find key
key_dec = pow(enc_sess_key, d, pub_rsa_key_n)   # key obtained here is in decimal
key_hex = hex(key_dec).split('x')[-1]       # converted the key to hex
print("Private Key:", key_hex)
########################################################################################################################
# Step 6: Using this key, decrypt the text on Cryptool 2
