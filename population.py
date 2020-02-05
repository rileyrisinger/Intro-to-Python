#Population
#Calculate population number
# Riley V. Risinger
#February 4th, 2020

#import modules
#Add any variables
#Ask for input
#Calculation of current population
#Print results

#birth time = 7 / 31536000
#death time = 13 / 31536000
#immigrant time = 35 / 31536000

#Inputs
years_input = int(input ("how many years?"))

population_number = 307357870 + ((7 - 13 + 35) * (years_input / 31536000))
print("Current population is", population_number, "people")
