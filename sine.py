# SINEs assignment using Pandas
# Riley Risinger
# March 30, 2020
# Practice using Pandas by manipulating a bed file


# import modules
import pandas as pd


# 1. Read file and Assign proper column names

print("###############")
print("Rename columns...")
families = ["Scaffold", "Start", "Stop", "Element", "Score", "Strand", "Family", "Sub-Family", "Divergence"]
bed = pd.read_csv ("aVan_rm.bed", names = families, sep= "\t")
bed.column=families
print(bed.head())


# 2. Determine Families

print("###############")
families = bed.Family.unique()
print("The families in this bed file are: ", families)


# 3. Create new dataframe using only SINE elements
print("###############")
bed_new=bed[bed['Family']=='SINE']
print(bed_new.head())
print("The new dataframe using only SINE elements is: ", '\n', bed_new.head())


# 4. Drop Strand and Score columns
print("###############")
bed_new=bed_new.drop(["Strand", "Score"], axis = 1)
print ("The dataframe after dropping 2 columns: ", '\n', bed_new.head())


# 5. Make new Length column
print("###############")
bed_new["Length"]=bed_new["Stop"]-bed_new["Start"]
print ("The dataframe after adding a Length column: ", '\n', bed_new.head())


# 6. Determine min, max, and mean for all SINEs
print("###############")
min = bed_new["Length"].min()
print ("The minimum value of SINEs is: ",min)
max = bed_new["Length"].max()
print ("The maximum value of SINEs is: ",max)
mean = bed_new["Length"].mean()
print ("The mean value of SINEs is: ",mean)


# 7. Determine min, max, mand mean for each SINE subfamily
print("###############")
min_sub = bed_new.groupby("Sub-Family")["Length"].min()
print ("The minimum value of the SINE sub families are: ", "\n", min_sub)
print("####")
max_sub = bed_new.groupby("Sub-Family")["Length"].max()
print ("The maximum value of the SINE sub families are: ", "\n", max_sub)
print("####")
mean_sub= bed_new.groupby("Sub-Family")["Length"].mean()
print ("The mean value of the SINE sub families are:    ", "\n", mean_sub)
print("###############")
