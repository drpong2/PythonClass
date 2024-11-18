import random
'''
#TIY9.1

Classes
Remember stringname.lower()? That's a *method* of the variable, which is of type string.
Any string you create is a class
string = "This is a test string" is from the class *str*
it has the methods defined by the string class

One of the methods of the str class is *isnumeric*
https://www.w3schools.com/python/python_ref_string.asp

inputvariable = input("Please enter a number: ")

if inputvariable.isnumeric():
	print(int(inputvariable))
else:
	print("That's not a number!")
'''
#9-1

class Restaurant:
	
	def __init__(self, restaurant_name, cuisine_type):
		self.name = restaurant_name
		self.cuisine = cuisine_type
		
	def describe_restaurant(self):
		print(self.name, self.cuisine)
	
	def open_restaurant(self):
		print("The restaurant is now open!")
		
my_restaurant = Restaurant("McDonalds","Fast Food")

my_restaurant.describe_restaurant()
string = "This is a test string"
print(string)
print(type(string))
print(type(my_restaurant))

my_restaurant.open_restaurant()

#9-2

restaurants = {"panda express": "chinese", "long john silver's": "fish", "phat noodle": "Thai", "Red Lobster": "Seafood"}
restaurant, cuisine = random.choice(list(restaurants.items()))
random_restaurant = Restaurant(restaurant, cuisine)
random_restaurant.describe_restaurant()
random_restaurant.open_restaurant()
#print(random.choice(list(restaurants.values())))

#9-3

class User:
	
	def __init__(self, first, last, manager, enabled, emailaddress):
		self.first = first
		self.last = last
		self.manager = manager
		self.enabled = enabled
		self.emailaddress = emailaddress
		self.name = self.last + ", " + self.first
		
	def describe_user(self):
		if self.enabled:
			accountaccess = "enabled"
		else:
			accountaccess = "disabled"
		print(self.name)
		print("Managed by:", self.manager)
		print("User is ", accountaccess)
		print("Email address:", self.emailaddress)
		
	def greet_user(self):
		print("Hello,", self.first.title(), self.last.title())
		

bob = User("bob","parr","Gilbert Huph",True,"bparr@megains.co")
bob.describe_user()
bob.greet_user()




