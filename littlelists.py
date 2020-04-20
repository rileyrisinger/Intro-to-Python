# littlelists.py
# Riley Risinger
# April 16, 2020

# for each task
#	1. do in loop and
#	2. do in list comprehension

# "The quick brown fox jumped over the lazy dog"

#############################

# 1. Count the number of spaces in the above string
## In loop
print("####################")
string = ("The quick brown fox jumped over the lazy dog")
spaces = 0
for i in string:
        if i ==" ":
                spaces = spaces + 1
print("In loop-")
print("The number of spaces in the phrase is:", spaces)

## In list comprehension
space_count = [i for i in string if i ==" "]
print("In list comprehension-")
print("The number of spaces in the phrase is:", len(space_count))



# 2. Find all the words that have the letter "o" in the above string
## In loop
print("####################")
words = string.split(" ")
words_with_o = []
for i in words:
        if i.count("o") > 0:
                words_with_o.append(i)
print("In loop-")
print( "The words that contain the letter 'o' in the phrase are:",  str(words_with_o))

## In list comprehension
words_with_o2 = [i for i in words if i.count('o') > 0]
print("In list comprehension-")
print("The words that contain the letter 'o' in the phrase are:", str(words_with_o2))



# 3. Find all the words that have at least 5 letters in the above string
print("####################")
## In loop
words_with5 = []
for i in words:
        if len(i) >=5:
                words_with5.append(i)
print("In loop-")
print("The words that contain at least 5 letters in the phrase are:", str(words_with5))

## In list comprehension
words_with5_2 = [i for i in words if len(i) >=5]
print("In list comprehension-")
print("The words that contain at least 5 letters in the phrase are:", str(words_with5_2))



#4 Find all the numbers from 1 to 1000 that have a "3" in it
print("####################")
## In loop
numbers = list(range(1,1001))
number_w3 = []
for i in numbers:
        if str(i).count('3') > 0:
                number_w3.append(i)
print("In loop-")
print("Numbers from 1-1000 that contain a 3 are:", str(number_w3))

## In list comprehension
number_w3_2 = [i for i in numbers if str(i).count('3') > 0]
print("In list comprehension-")
print("Numbers from 1-1000 that contain a 3 are:", str(number_w3_2))
print("####################")
