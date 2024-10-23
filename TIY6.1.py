#6-1 Persons - print each piece of info: first_name, last_name, age, city
persons = []
bilbo={'first_name' : 'bilbo', 'last_name' : 'baggins', 'age' : 111, 'city' : 'The Shire'}
frodo={'first_name' : 'frodo', 'last_name' : 'baggins', 'age' : 23, 'city' : 'The Shire'}
persons.append(bilbo)
persons.append(frodo)
print(persons)

print(bilbo['age'])



#6-2 Favorite Numbers - 5 names, use them as keys for a favorite number for each person

favorite_numbers = {
    'jen' : 58, 
    'sarah' : 23, 
    'edward' : 12, 
    "phil" : 8
}

print(favorite_numbers)

#6-3 Glossary - Dictionary of methods and what they do
python_glossary = {
    'print':"Function, Prints data to the screen. can use f-string literals to format and include variables",
    'range':"Function, takes 1-3 arguments and generates a list of numbers based on the arguments passed",
    'for':"Control function, used for iterating through a list or range",
    'if':"control function, used for comparisons, including checking to see if a non-integer value is in a set",
    'append':"method for lists to add an additional value",
    'sorted':"function for temporarily sorting a list or dictionary in alphabetical or numerical order"
}
for key, value in python_glossary.items():
    print(f"\nKey: {key}")
    print(f"\tValue: {value}")

