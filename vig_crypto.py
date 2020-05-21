'''
-----------------------------------------------------------------------
 Date: 21.Mai 2020
 Das Ziel der Aufgabe: Dechiffrieren Sie den Text (Vignere Chiffre)
 -----------------------------------------------------------------------
'''

# section 1: get the cipher text
w_txt = "C:\\Users\\dell\\Downloads\\encrypted_vig.txt"
fptr = open(w_txt, "r")
cipher_text = fptr.read()               # cipher_text holds the encrypted text
cipher_text_len = len(cipher_text)      # cipher_text_len holds the length of the encrypted text

#section 2: check for the occurences and store them in a file
fw = open("output.txt", "a")            # this file holds the information about
                                        # sequence occurences
sequence_list = []
i = 0                               
j = 0
sequence_dict = {}                      # this dictionary to hold sequences
                                        # with number of repetitions
for i in range(cipher_text_len):
    for j in range(cipher_text_len):
        sequence = cipher_text[i:j]         # sequence holds the sub-string
                                            # which will be searched in main string
    
        found = cipher_text.find(sequence)  # to find if the sequence
                                            # appears in the cipher text
                                            
        rep = cipher_text.count(sequence)   # rep holds the number of times
                                            # sequence has been repeated in the main text
                                        
        if found != -1 & rep-1 != 0:        # this indicates match is found
            if sequence in sequence_list:       # this is for eliminating duplicate sequences
                continue
            else:                               # this is for unique sequences found
                fw.write("-----Positons recorded for:")
                fw.write(sequence)
                fw.write(str(found))
                fw.write(" ")
                sequence_list.append(sequence)
                sequence_dict[sequence] = rep;  # store sequence and repetition number
        else:                               # this indicates match not found
            continue
        
        j = j+1
        fw.write("\n\n")
    i = i+1
fw.write("------------------------------------------------------------------------------------")
for k in sequence_dict:                 # write the values of the dictionary
                                        # to the output.txt file
    fw.write(str(k))
    fw.write("-->")
    fw.write(str(sequence_dict[k]))
    fw.write("\n\n")
fw.close()



