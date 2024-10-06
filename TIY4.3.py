#TIY4.3.py

#4-10 Slices
pizzas=["sausage","pepperoni","meatlovers"]
for pizza in pizzas:
  print(f"I love {pizza}")
print("I love any kind of pizza, really")
print(f"the first three items in the list are: {pizzas[:3]}")
print(f"three items from the middle of the list are: {pizzas[0:3]}")
print(f"The last 3 items from the list are {pizzas[-3:]}")


#4-11 My pizzas, your pizzas
pizzas=["sausage","pepperoni","meatlovers", "hawaiian"]
friend_pizza = pizzas[:]
friend_pizza.append("supreme")
print("my favorite pizzas are:")
for pizza in pizzas:
  print(f"{pizza}")
#print("I love any kind of pizza, really")
print("my friend's favorite pizzas are: ")
for pizza in friend_pizza:
    print(f"{pizza}")

#4-12 More Loops
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)