#6.2 


#6-4 Glossary 2
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


#6-5 Rivers - key/value pair of river:country - 3 values - loop through and print a sentance about each river
#second loop for each river name
#third loop for each country name
rivers={"Mississippi" : "US", "Nile" : "Egypt", "Seine" : "Germany"}
for river in rivers:
    for country in rivers.values():
        print(f"{river} is in {rivers[river]}")
for river in rivers:
    country = rivers[river]
    print(f"{river} is in {country}")
for river in rivers.keys():
    print(f"the river {river} is in this list.")
for country in rivers.values():
    print(f"the country {country} is in this list.")


#6-6 Polling - use the code in favorite_language
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

coders = ["albert", "jen", "thomas", "sara", "nikola", "edward", "blaise", "phil"]
for coder in coders:
    if coder in favorite_languages.keys():
        print(f"Than you, {coder}, for taking the survey!")
    else:
        print(f"Please enter your favorite language, {coder}")



#the below is both a precursor to, and a poor man's object oriented programming.
#Classes in chapter 9 will go into that in more detail

'''
# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
➊ for alien_number in range(30):
➋
new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
➌
aliens.append(new_alien)
'''

#Insert Mines of Moria joke here
'''
You should not nest lists and dictionaries too deeply. If you’re nesting items
much deeper than what you see in the preceding examples or you’re working
with someone else’s code with significant levels of nesting, most likely a simpler
way to solve the problem exists.
'''

