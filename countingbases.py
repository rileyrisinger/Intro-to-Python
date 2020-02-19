import random
bases = ["A", "C", "T", "G"]
sequence = random.choices(bases, k=100)
print(sequence)
acount = sequence.count("A")
gcount = sequence.count("G")
countac = sequence.count("A") + sequence.count("C")
print("The number of A's   = ", acount, '\n' "The number of G's = ", gcount, '\n', "A's + C's = ", countac)
