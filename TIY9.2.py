

#9-4
class Restaurant:
	
	def __init__(self, restaurant_name, cuisine_type):
		self.name = restaurant_name
		self.cuisine = cuisine_type
		self.number_served = 0
		
	def describe_restaurant(self):
		print(self.name, self.cuisine)
	
	def open_restaurant(self):
		print("The restaurant is now open!")
	
	def set_number_served(self, setvalue):
		self.number_served = setvalue
	
	def increment_number_served(self, increment):
		self.number_served += increment
		
my_restaurant = Restaurant("McDonalds","Fast Food")

my_restaurant.describe_restaurant()

my_restaurant.open_restaurant()

my_restaurant.set_number_served(25000000)
print("Number served is", my_restaurant.number_served) 
my_restaurant.increment_number_served(7)
print(my_restaurant.number_served)


#9-5

class User:
	
	def __init__(self, first, last, manager, enabled, emailaddress):
		self.first = first
		self.last = last
		self.manager = manager
		self.enabled = enabled
		self.emailaddress = emailaddress
		self.name = self.last + ", " + self.first
		self.login_attempts = 0
		
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
	
	def increment_login_attempts(self):
		self.login_attempts += 1
		
	def reset_login_attempts(self):
		print("Resetting login attempts")
		self.login_attempts = 0
		

bob = User("bob","parr","Gilbert Huph",True,"bparr@megains.co")
bob.describe_user()
bob.greet_user()

passwordattempts = 0
print("Three incorrect passwords were tried:")
while passwordattempts < 3:
	bob.increment_login_attempts()
	passwordattempts += 1
print(f"{bob.login_attempts} passwords were tried before the correct password was entered")
print("Correct password entered. Logging in.")
bob.reset_login_attempts()
