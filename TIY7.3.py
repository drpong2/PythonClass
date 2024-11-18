#TIY7.3
'''
7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches.
Then make an empty list called finished_sandwiches. Loop through the list of sandwich
orders and print a message for each order, such as I made your tuna sandwich. As each
sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been
made, print a message listing each sandwich that was made.
'''
sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")
'''
7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich
'pastrami' appears in the list at least three times. Add code near the beginning of your
program to print a message saying the deli has run out of pastrami, and then use a while loop
to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami
sandwiches end up in finished_sandwiches.
'''
sandwich_orders = ['veggie', 'pastrami', 'grilled cheese', 'pastrami', 'turkey', 'pastrami', 'roast beef']
finished_sandwiches = []

print("We're out of pastrami")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)


print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")
'''
7-10. Dream Vacation: Write a program that polls users about their dream vacation. Write a
prompt similar to If you could visit one place in the world, where would you go? Include a block of
code that prints the results of the poll.
'''
poll_results = {}
print("Welcome to my dream vacation quiz!")
name = input("please enter your name: ")
place = input(f"Thank you, {name.title()}! Where would you like to go for your dream vacation?")
poll_results[name] = place
input_store = input("press p to print, c for another data entry, q to quit")
while 'c' in input_store:
	name = input("please enter your name: ")
	place=input(f"Thank you, {name.title()}! Where would you like to go for your dream vacation?")
	poll_results[name] = place
	input_store = input("press p to print, c for another data entry, q to quit")
while 'p' in input_store:
	print("The poll results are as follows:")
	print(poll_results)
	input_store = input("press p to print, c for another data entry, q to quit")
while 'q' in input_store:
	break	
