#=
# Das Ziel des Programms: Calculate d for RSA-AES Decryption
# Date: 13.Juni 2020
# Die Sprache des Programms: Julia
=#

#=
The Euler Totient function is calculated in Python and is fed as input to this
program. The value of e is given already. The d is calculated here using
The extended Euclid's algorithm. The output of this
=#

# input the parameters
phi_n_in = parse(BigInt, input("Enter the phi value: "))
e_in = parse(BigInt, input("Enter the e value: "))

# set up the initial conditons for the Extended Euclid's algorithm
r1c1 = phi_n_in
r1c2 = phi_n_in
r2c1 = e_in
r2c2 = 1
d = 0

# Calculate the private key using EEA
while (true)

    global r1c1
    global r1c2
    global r2c1
    global r2c2
    global d

    res11 = div(r1c1, r2c1)

    res12 = r2c1 * res11
    res21 = r2c2 * res11

    new_r2c1 = r1c1 - res12
    new_r2c2 = r1c2 - res21

    if new_r2c2 < 0
        new_r2c2 = mod(new_r2c2, phi_n_in)
    end

    r1c1 = r2c1
    r1c2 = r2c2
    r2c1 = new_r2c1
    r2c2 = new_r2c2

    if r2c1 == 1
        d = r2c2
        break
    end
end

# Display the key
print("\n")
println("The value of d is: ",d)
