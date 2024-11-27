import menu
import json
import ast
import base64 as b64
filename = 'userinfo.txt'
users = {}

def newuser():
	user1 = input("Please enter a username:\n")
	password = passwordvalidate()
	hashable = str.encode(password)
	hashed = b64.b64encode(hashable)
	storable = hashed.decode()
	users[user1] = storable
	with open(filename, 'a') as file_object:
		json.dump(users, file_object)
		file_object.write("\n")
		file_object.close()

def loadusers():
	try:
		with open(filename) as file_object:
			userbyline = file_object.readlines()
			for line in userbyline:
				user1 = ast.literal_eval(line)
				for key, value in user1.items():
					users[key] = value
		file_object.close()
	except(FileNotFoundError):
		print("No users found: Creating new user")
		newuser()
		
def uservalidate():
	attempts = 0
	while attempts <= 3:
		user=input("Please enter a username: ")
		if user in users.keys():
			#print(f"User found: {user}, password is {users[user]}")
			passwordauth(user)
			return True
		elif attempts >= 3:
			break
		else:
			("user not found!")
			attempts += 1

def passwordauth(username):
	tries = 3
	while tries > 0:
		password = input("Please enter password: ")
		hashable = str.encode(password)
		hashed = b64.b64encode(hashable)
		storable = hashed.decode()
		if users[username] == storable:
			menu.mainloop()
			break
		else:
			tries -= 1
			print(f"Password incorrect! {tries} remaining")

def passwordvalidate():
	password = input("Please enter a password: ")
	pwvalidate = input("please re-enter the password: ")
	while pwvalidate != password:
		print("Passwords do not match!")
		password = input("Please enter a password: ")
		pwvalidate = input("Please re-enter the password: ")
	return password



'''

print("1 to load, 2 to create")

userinput = input(":\>")
if userinput == '1':
	try:
		with open(filename) as file_object:
			file_object.close()
		loadusers()
		#This needs to be moved out of a try/catch block
		uservalidate()
	except(FileNotFoundError):
		print("No users currently found! Please create a new user")
	
elif userinput == '2':
	newuser()

	with open(filename) as file_object:
		namelist = json.load(file_object)
		print(namelist)
		input("press enter to continue")
		username = input("please enter a username: ")
		while username in namelist:
			username = input("That username is taken, please try "
			"another, or press 'q' to return to the login screen: ")
			if username.lower() == 'q':
					break


users = {}
user1 = input("Please enter a username:\n")
password = passwordvalidate()

users[user1] = password
print(users)
with open(filename, 'a') as file_object:
	json.dump(users, file_object)
	file_object.write("\n")
	file_object.close()
	
with open(filename) as file_object:
	users = json.load(file_object)
	print(users)
	print(type(users))
		
'''
'''
		linelist = dic(lines)
		print(type(linelist))
		userlist = json.loads(linelist)
		
		userdict = ast.literal_eval(userlist)
		print(type(userdict))
		'''

		



'''
#newuser()
namelist = {}
menu = int(input("1. New user\n2. Load user"))
if menu == 1:
	username = input("please enter a username: ")
	while username in namelist:
		username = input("That username is taken, please try "
		"another, or press 'q' to return to the login screen: ")
		if username.lower() == 'q':
				break
	password = input("Please enter a password: ")
	pwvalidate = input("please re-enter the password: ")
	while pwvalidate != password:
		print("Passwords do not match!")
		password = input("Please enter a password: ")
		pwvalidate = input("Please re-enter the password: ")

	#hashable = b64.encode_base64(password)
	hashable = str.encode(password)
	hashed = b64.b64encode(hashable)
	print(hashed)
	storable = hashed.decode()
	userinfo = {username: storable}
	with open(filename, 'a') as file_object:
		json.dump(userinfo, file_object)
		json.dump("\n",file_object) 
		file_object.close()
elif menu == 2:
	with open(filename, 'r') as file_object:
		namelist = json.load(file_object)
		print(namelist)
'''
