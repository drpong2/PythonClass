#TIY7.1
from random import choice as c
#importing libraries - you can import the whole library, or one specific part. You can also give that specific part an alias
'''
Issues with input() command in sublime
Sublime will not accept user input
You can save your code and run it from the command line
This requires familiarity with the file structure of your Operating System

input()
int()
while loops
similar to for loops - check for a condition to be true
while heath > 0 print("stayin' alive")
using a flag - just a variable to check to see if the value has changed
Using break to exit a loop
    break keyword just tells the program to exit the loop it is in, whether 'for' loop or 'while' loop
for number in range(10):
    print(number)
    if number == 5:
        break
continue
    do nothing, proceed to the next step/iteration through the loop

Every programmer accidentally writes an infinite while loop from time to
time, especially when a program’s loops have subtle exit conditions.
I wrote my first infinite loop in 2005 with qbasic

10 print "Hello world"
20 GOTO 10
30

'''
#7-1 Rental car
available_cars = ["honda", "chevy", "gmc", "lexus"]
desired_car = input("Please enter desired car brand would you like for your rental:")
print("Thanks, let me check if we have that one.")
if desired_car.lower() in available_cars:
    print(f"Yep, we have {desired_car} models available for rental!")
else:
    print(f"I'm sorry, we don't have any {desired_car} models available")
    carsub = c(available_cars)
#The way the above line would look if we just imported the whole `random` module:
# carsub = random.choice(available_cars)
    print(f"I can get you into a {carsub} today")

#7-2 Restaurant seating: Ask for party size, anything larger than 8 has to wait
tablesize = input("Thanks for dining at Chez Martin tonight! How many are in your party?\n")
tablesizenum = int(tablesize)
if tablesizenum > 8:
    print("I'm terribly sorry, but there is a slight wait for a party of that size")
elif tablesizenum < 1:
    print("I'm... not sure how to work with that?")
else:
    print("A waiter will be by to show you to your table shortly.")


#7-3 multiples of 10
#get a number from the user
usernum = input("Please enter a number, and I will tell you if it is divisible by 10:\n")
#if usernum[-1:] == '0':
actualnum = int(usernum)
if actualnum % 10 == 0:
    print("The number is divisible by 10"")
else:
    print("The number is not divisible by 10")
'''
7-1. Rental Car: Write a program that asks the user what kind of rental car they would like.
Print a message about that car, such as “Let me see if I can find you a Subaru.”

7-2. Restaurant Seating: Write a program that asks the user how many people are in their
dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a
table. Otherwise, report that their table is ready.
7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a
multiple of 10 or not.
'''
