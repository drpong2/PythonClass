from time import sleep

class Car:
	def __init__(self, make, model, year):
		self.manufacturer = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	def get_descriptive_name(self):
		long_name = f"{self.year} {self.manufacturer} {self.model}"
		return long_name.title()
	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it.")
	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		self.odometer_reading += miles

class Battery:
	def __init__(self, battery_size=75):
		self.battery_size = battery_size
	
	def describe_battery(self):
		print(f"This car has a {self.battery_size}-kWh battery.")

	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315
		print(f"This car can go about {range} miles on a full charge.")
		
	def upgrade_battery(self):
		if self.battery_size == 75:
			self.battery_size = 100
		elif size.battery_size == 100:
			print("This is already the extended range battery")

class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""

	def __init__(self, make, model, year):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to an electric car.
		"""
		super().__init__(make, model, year)
		self.battery_size = 75
		self.battery = Battery()
		self.charge = charge
			
	def fill_gas_tank(self):
		print("This car doesn't need a gas tank!")
		
	def charge_battery(self):
		charge = 0
		while charge < 100:
			print(f"Charging battery {charge}%")
			charge += 10
			sleep(5) 
	'''
	Challenge code - get the battery charge level
	def get_charge(self):
		print(charge)
	'''
			
	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()	
my_tesla.get_charge()
my_tesla.charge_battery()
my_tesla.battery.get_range()
print("Upgrading battery...")
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
