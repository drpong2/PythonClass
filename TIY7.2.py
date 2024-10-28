#TIY7.2

'''
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings
until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add
that topping to their pizza.
'''
toppingarray = []
print("please enter your topping for the pizza, or type 'quit' to exit:")
textinput = input("")
while textinput.lower() != "quit":
    toppingarray.append(textinput)
    textinput = input(f"{textinput} will be on your pizza, anything else?\n")
print("Your pizza has the following toppings:")
for topping in toppingarray:
    print(f"\t - {topping}")
    
'''
7-5. Movie Tickets: A movie theater charges different ticket prices depending on a person’s
age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is
$10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age,
and then tell them the cost of their movie ticket.
'''
partyarray = []
partyprice = []
party = input("welcome to the show! How many tickets today?\n")
partynum = int(party)
if partynum < 1:
    print("not a real number")
elif partynum == 1:
    age = input("How old are you?")
elif 1 < partynum < 12:
    for person in range(partynum):
        indexnum = person + 1
        age = input(f"person {indexnum}, how old are they?")
        if age == '':
            age = 0
        partyarray.append(age)
elif party > 11:
    print("please call the office for pricing")

for person in partyarray:
    personage = int(person)
    if int(person) < 3:
        partyprice.append(0)
    elif 2 < personage < 13:
        partyprice.append(10) 
    elif personage > 12:
        partyprice.append(15)

print("Total cost for the theater trip:")
totalcost = sum(partyprice)
print(f"${totalcost}")
        
'''

7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 that do each
of the following at least once:
Use a conditional test in the while statement to stop the loop.
Use an active variable to control how long the loop runs.
Use a break statement to exit the loop when the user enters a 'quit'
value.
'''
textinput = ""
toppingarray = []
print("please enter your topping for the pizza, 5 toppings expected:")
increment = 1
textinput = input("")
while increment < 6:
    toppingarray.append(textinput)
    textinput = input(f"{textinput} will be on your pizza, anything else?\n")
    increment += 1
print("Your pizza has the following toppings:")
for topping in toppingarray:
    print(f"\t - {topping}")
'''
7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press CTRL-C or
close the window displaying the output.)
'''
var = 1
while var < 2:
    print("This is the song that never ends\nIt just goes on and on my friend\n\
some people started singing it not knowing what it was\n\
and now they're stuck forever simply just because\n")




