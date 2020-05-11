# GC-Content-ArgParse.py
# April 29, 2020
# Riley Risinger
# Calculate the GC content of a random sequence using Argparse


# import modules (random and argparse definitely both needed)
import argparse
import random
import matplotlib.pyplot as plt

# the required lines of code for Argparse
#########################################################################
############################### ARGUMENTS ###############################
#########################################################################

ap = argparse.ArgumentParser()
ap.add_argument("-l", "--LENGTH", required=True, type=int, help="Enter the length of the sequence")
ap.add_argument("-s", "--SMALL", required=True, type=int, help="Enter the size of the small sequences")
args = vars(ap.parse_args())


# 1. Argparse the size of random sequence
bases = ['A', 'T', 'G', 'C']
seq = random.choices(bases, k = args["LENGTH"])
DNA_seq = ''.join(seq)
print("The randomly generated DNA sequence is: \n", DNA_seq)



# 2. Argsparse the size of smaller sequences (<50 bp I'm guessing)
smaller_seq=[]
for i in range (0, args["LENGTH"], args["SMALL"]):
        smaller_seq.append(DNA_seq[i: i + args["SMALL"]])
print("The size of the smaller sequences are, \n", smaller_seq)


# 3. Create a histogram for Gccontent
# Calculate GC content
def GC(smaller_seq):
        GC_number = ((smaller_seq.count("G") + smaller_seq.count("C"))/100)*100
        return (GC_number)

GC_content = [GC(index) for index in smaller_seq]

print("The GC content for the smaller sequences is: \n", GC_content)

#Histogram
plt.hist(GC_content)
plt.grid(axis='y', alpha=0.75)
plt.ylabel('Frequency', fontsize=12)
plt.xlabel('GC-content', fontsize=12)
plt.title('Histogram of GC-content', fontsize=15)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()
