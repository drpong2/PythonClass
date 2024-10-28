import random
#TIY6.3.py

#6-7 
persons = []
bilbo={'first_name' : 'bilbo', 'last_name' : 'baggins', 'age' : 111, 'city' : 'The Shire'}
frodo={'first_name' : 'frodo', 'last_name' : 'baggins', 'age' : 23, 'city' : 'The Shire'}
skywalker={"first_name" : "luke", 'last_name':'skywalker','age':19, 'city':'mos espa'}
persons.append(bilbo)
persons.append(frodo)
persons.append(skywalker)
for person in persons:
        fullname = f"{person['first_name']} {person['last_name']}"
        age = person['age']
        city = person['city']
        print(f"name is {fullname}, age is {age}, and city is {city}")

#6-8 pets


#6-9



#6-10

numjen = []
for number in range(4):
    numjen.append(range(1,11))

favorite_numbers = {
    'jen' : numjen
    'sarah' : 23, 
    'edward' : 12, 
    "phil" : 8
}

#6-11 cities - country, approx pop, one fact (lat/long)

