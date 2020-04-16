# genes.py
# Riley Risinger
# April 14, 2020

# Goal: Determine the length of large genes on mRNA strand
# Assumptions: Genes are recognized as segments of RNA separated by start codon AUG

####################

# 1. Generate a random RNA sequence into a STRING 1000 bp long
print ("####################")
import random
bases = ['A', 'G', 'U', 'C']
seq = random.choices(bases, k=1000)
mRNA = ''.join(seq)
print("The randomly generated 1000bp RNA sequence is \n", mRNA)


# 2. Create a list of genes that are separated by start codon
print ("####################")
genes = mRNA.split("AUG")
print ("The list of genes separated by the start codon AUG in the sequence: \n", genes)


# 3. Create a list of large genes (>50bp)
# make a for loop for length, where for every gene (i) in "genes" that >50bp, put it in list
print ("####################")
large_genes=[]
for i in genes:
        if len(i)>50:
                large_genes.append(i)
print("The list of genes with >50bp is \n" , large_genes)


# 4. Determine length of large genes
# make another for loop to calculate length of "i" in large genes
print ("####################")
for i in large_genes:
        print ("The length of one of the large genes is \n", len(i))
