# genecomprehension.py
# Riley Risinger
# April 19, 2020

# Goal: determine length of large genes on mRNA stran
# Assumptions: Genes are recognized as segments of RNA separated by start codon AUG


## similar to the genes assignment, but use list comprehension.
## Steps 1, 2 and 4 copied from previous assignment

######################################################################

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


# 3. Create a list of large genes (>50bp) using List Comprehension
### loop version
# large_genes=[]
# for i in genes:
        # if len(i)>50:
                # large_genes.append(i)
# print("The list of genes with >50bp is \n" , large_genes)
print("####################")
### list comprehension version
large_genes = [i for i in genes if len(i) > 50]
print("The list of genes with >50bp using list comprehension is: \n", large_genes)


# 4 Determine length of large genes
print ("####################")
for i in large_genes:
        print ("The length of one of the large genes is: \n", len(i))
