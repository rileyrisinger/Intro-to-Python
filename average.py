##it works but I have to enter each number one by one, need help fixing that

#average.py
#Riley Risinger
#February 29, 2020

#define num, what I'm calling the input, restricting to integers
num = int(input('How many numbers: '))
total_sum = 0

#make the for loop, defining terms for average equation later
for n in range(num):
        numbers = float(input('Enter number : '))
        total_sum += numbers

#now calculate average
avg = total_sum/num
print('The average of ', num, ' numbers equals :', avg)
