import menu
import json
import ast
import base64 as b64
filename = 'userinfo.txt'
users = {}
#1 Initialize the Users dict and set the filename, in addition to all the module imports

def newuser():
	user1 = input("Please enter a username:\n")
	password = passwordvalidate()
	#2 Get the username from the user and the password from the passwordvalidate function
	hashable = str.encode(password)
	hashed = b64.b64encode(hashable)
	storable = hashed.decode()
	#3 This code takes the password and converts it to a base64 string, to obfuscate the password in the text file - storable is the password value as a base64 string
	users[user1] = storable
	#4 This sets the key user1 (username) with the value base64 password
	with open(filename, 'a') as file_object:
		json.dump(users, file_object)
		file_object.write("\n")
		#5 this dumps the users dictionary to the file
		file_object.close()

def loadusers():
	try:
		with open(filename) as file_object:
			userbyline = file_object.readlines()
			for line in userbyline:
				user1 = ast.literal_eval(line)
				#6 This line actually is needed to parse the strings written from the file back into a dictionary
				for key, value in user1.items():
					users[key] = value
					#7 This loads up the the dictionary from our file into a dictionary in the program
		file_object.close()
	except(FileNotFoundError):
		print("No users found: Creating new user")
		newuser()
		#8 If the file is not found, a new user is created and the file is written with data.
		
def uservalidate():
	attempts = 0
	#9 This initializes a control variable for our while loop
	while attempts <= 3:
		user=input("Please enter a username: ")
		if user in users.keys():
			#10 We check to make sure the user is valid by comparing the inputted user to the key entries in our user dictionary
			passwordauth(user)
			#11 if the user is valid, we call password auth passing the username
			return True
		elif attempts >= 3:
			break
		else:
			("user not found!")
			attempts += 1
			#12 increments the control variable so we don't stay in the while loop forever

def passwordauth(username):
	tries = 3
	#13 initializing a control variable for the while loop, the username is passed in from uservalidate.
	while tries > 0:
		password = input("Please enter password: ")
		hashable = str.encode(password)
		hashed = b64.b64encode(hashable)
		storable = hashed.decode()
		#14 When we get the password from the user, we need to hash it to make sure it matches the stored password hash
		if users[username] == storable:
			menu.mainloop()
			#15 If the password value for the username key in the users dictionary matches the password that was just entered, call the mainloop function from menu.py
			break
			#16 when the main menu loop is exited, break out of the password authentication attempt. Without this, you'd keep your number of password attempts after exiting the program
		else:
			tries -= 1
			print(f"Password incorrect! {tries} remaining")
			#17 if the password isn't correct, subtract one from our control variable

def passwordvalidate():
	password = input("Please enter a password: ")
	pwvalidate = input("please re-enter the password: ")\
	#18 Take two passwords as separate strings
	while pwvalidate != password:
		print("Passwords do not match!")
		password = input("Please enter a password: ")
		pwvalidate = input("Please re-enter the password: ")
		#19 Compare the passwords. If they they don't match, keep asking for two passwords'
	return password
	#20 Password gets returned as a value so you can do the following: passwordvariable = passwordvalidate()

