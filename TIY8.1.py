#TIY8.1
from random import choice
#terms from last week: casting, data types, functions, modules, classes

#function call using positional arguments, keyword arguments to match the accepted parameters/explicitly defined arguments
# default function arguments are described during definition, and these can be overridden by passing new arguments.
#build_person function allows the user to help build the dictionary 
#greeter.py - example of how to use a while loop with escape conditions
#printing_models.py - What happens if you pass a string as argument instead of a list? How would you make sure you get something usable


#8.1 - welcome message - display_message() - one sentence, call the function
def display_message():
    '''Displays a message'''
    print("Today we're learning about functions.")
    print("Passing values to functions, and importing modules and functions.")

display_message()


#8.2 Favorite_book() - accepts `title` parameter, print a message
def favorite_book(title):
    print(f"One of my favorite book series is {title}")

booklist = ["Chronicles of Fid","Star Wars", "Lord of the Rings", "Chronicles of Narnia"]
favorite_book(choice(booklist))
3


