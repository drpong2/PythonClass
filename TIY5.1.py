#5.1 conditional tests
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

#10 tests go here if I have time

#5.2 More conditional tests
animals=["Dog","cat","elephant"]
answer=["would","would","would not"]
goodpets=["Dog","cat","gecko"]

health = 10
print("Is health == '10'? I predict false")
print(health == '10')
print(f"is {10} the same as '10'?")
print(10 == '10')


name = "Steve"
print("Is name == 'steve'? I predict false")
print(name == 'steve')
#tests using the lower() method
print("Is name == 'steve'? I predict true")
print(name.lower() == 'steve')
print("Is health greater than 10? I predict True")
print(health > 10)
print("Is health between 5 and 15? I predict True")
print(5 < health < 15)
#numerical tests involving equality and inequality, greater than/less than, ge/le
#tests using the and keyword and the or keyword
given_name = "john"
print("Is given name John (capitalized or not)? I predict true")
print(given_name == "john" or given_name == "John")
#test whether an item is in a list
potentialpet = "gecko"
print(f"Is {potentialpet} a good pet? I predict true")
if potentialpet in goodpets:
    print(True)
else:
    print(False)
#test whether an item is not in a list
badpet="elephant"
print(f"Is elephant a good pet? I predict false")
if badpet in goodpets:
    print(True)
else:
    print(False)

#equality and inequality with strings

