speciesa1,speciesa2 = input("Enter 1st species: ").split()
speciesb1,speciesb2 = input("Enter 2nd species: ").split()
speciesc1,speciesc2 = input("Enter 3rd species: ").split()
newspeciesa = (speciesa1[0:3].upper() + speciesa2[0:3].upper())
newspeciesb = (speciesb1[0:3].upper() + speciesb2[0:3].upper())
newspeciesc = (speciesc1[0:3].upper() + speciesc2[0:3].upper())

answer = "There are three species of bats: "
print( "There are three species of bats: ", '\n', newspeciesa, '/n', newspeciesb, '\n', newspeciesc)
