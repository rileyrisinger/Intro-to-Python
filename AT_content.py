# AT Content Algorithm
# Riley Risinger
# March, 2, 2020
# Program that will print out the AT content of a DNA sequence

#Enter the DNA sequence
dna_seq1 = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

#Count amount of A's in the sequence using loop and else/if statments
count = 0
for i in dna_seq1:
        if i == "A":
                count = count +1
        elif i == "T":
                count = count + 1

#Print Statment
print ("AT count of the DNA sequence is : " + str(count))
