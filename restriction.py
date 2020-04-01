#
# Riley Risinger
# March 28, 2019
# Create an Algorithm to act as a restriction enzyme and calculate fragment sizes

# Enter the DNA sequence
dna_str = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

# Enter the restriction site
rest_str = "AATTC"

# Find where restriction site is located in the string
rest_site = dna_str.find(rest_str)

# Find Sequence length
totallen = len(dna_str)

# Calculate size of resulting fragments after EcoR1 cuts at restriction site
fragment_1 = rest_site + 1
fragment_2 = totallen - fragment_1

# Print Statement
print("The length of each fragment after digestion by the EcoR1 enzyme is", fragment_1, "and",  fragment_2, "respectively.")

