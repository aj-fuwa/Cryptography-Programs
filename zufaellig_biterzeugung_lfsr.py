'''
# Das Ziel des Programms: LFSR-Pseudo Random Noise Generation
# Date: 1.Juni 2020
# Die Sprache des Programms: Python
'''
########################################################################################################################
# Step 1: Input the basic parameters required for the LFSR PRNG
# Step 1.1: Get the desired number of output bits
num_output_bits = int(input("Enter the number of bits to be generated: "))
output_bits = []    # this list will hold all the output bit values

# Step 1.2: Get the generator polynomial
pos_of_ones = []    # this list will hold the position of 1s in generator polynomial
gen_poly = []       # this list will hold our generator polynomial

# read the generator polynomial from the gen_poly.txt file
f_ptr = open('C:\\path\\to\\generator polynomial where it is in 1 and 0 form')
gen_poly = f_ptr.readlines()
gen_poly = [int(gen_poly_var) for gen_poly_var in gen_poly]
f_ptr.close()
print("The generator polynomial is (in the form of 1 and 0): ", gen_poly)

# this is for displaying the generator polynomial in g(x) form
print("The generator polynomial is (in the form of x): g(x) = ", end = " ")
for index in range(len(gen_poly)):
    if(gen_poly[index] != 0):
        pos_of_ones.append(index)
        print("+ x^",index+1, end = " "),
print("+ 1\n")

# get the total count of the flipflops i.e., highest power of generator poly
ff_count = len(gen_poly)
print("Total number of flipflops used in this LFRS-PRNG: ", ff_count)

# Step 1.3: Get the initial state of the flipflops
init_state_ff = []      # this list stores the initial values of the flipflops

# read the initial state of the flipflops from the file init_state_ff.txt
f_ptr = open('C:\\path\\to\\file\\where initial state of the flipflops')
init_state_ff = f_ptr.readlines()
init_state_ff = [int(init_state_values) for init_state_values in init_state_ff]
f_ptr.close()
print("The initial values of the flipflops are: ", init_state_ff)
########################################################################################################################
# Step 2: Generate the bits
current_state_ff = []       # holds the current state of the flipflops
next_state_ff = []          # holds the next state of the flipflops
current_state_ff = init_state_ff    # in the first round, current state will have initial values
next_bit = 0            # this is bit that will be calculated

# write the output bits in out_bits.txt file
f_ptr_output = open('C:\\path\\to\\file\\where output bits will be written', 'w')

for main_loop_index in range(num_output_bits):
    f_ptr_output.write(str(current_state_ff[-1]))   # write the last bit from the list
                                                    # this is the output of the LFSR

    # calculate the bit based on the generator poly
    for inner_index in range(len(current_state_ff)):
        if (inner_index in pos_of_ones):
            next_bit = next_bit ^ current_state_ff[inner_index]

    inner_index = 0         # clear this for the next cycle use
    next_state_ff.append(next_bit)      # add the calculated bit at the
                                        # first position of the next state of flipflops

    next_bit = 0            # clear this for the next cycle use

    # copy contents from current_state_ff to next_state_ff
    # and then delete the last element from the next_state_ff
    # since current_state_ff has 16 bits and those 16 will be appended to next_state_ff
    # that will make 17 bits in next_state_ff
    for inner_index in range(len(current_state_ff)):
        next_state_ff.append(current_state_ff[inner_index])
    del next_state_ff[-1]

    # uncomment lines 78 and 80 to see all state values of the flipflops
    #print("Next state:", next_state_ff, "length: ", len(next_state_ff))
    current_state_ff = next_state_ff        # this is the updated current state of flipflops
    #print("New current state is: ", current_state_ff)

    next_state_ff = []          # clear the list

f_ptr_output.close()
