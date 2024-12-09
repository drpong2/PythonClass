# Please fill in each comment line with comments

def listapps():
	listvar = True
	#1
	while listvar:
		#2
		print("1. Mail\n2. browser\n3. games\n4. programming language\n5. return")
		entry = input("Please enter your selection: ")	
		if entry == '5':
			listvar = False
			break
			#3
		elif entry == '4':
			languages = ['C++', 'Java', 'Rust', 'Python','Powershell','javascript']
			for language in languages:
				print(language, '\n')
			#4
		elif entry == '3':
			games = ['Galaxy of Heroes','Valheim','Minecraft','fortnite','clash of clans']
			for game in games:
				print(game, '\n')
		elif entry  == '2':
			browsers = ['chrome','edge','opera gx','safari','vivaldi','brave']
			for browser in browsers:
				print(browser, '\n')
		elif entry == '1':
			mailapps = ['outlook','mail','microsoft mail','google mail','thunderbird']
			for app in mailapps:
				print(app,'\n')
		else:
			print("That entry is invalid. Please try again")
	
def getroles():
	listvar = True
	#5
	print("1. user\n2. admin\n3. moderator\n4. List permissions\n5. return")
	while listvar == True:
		entry = input("Please enter your selection: ")
		if entry == '5':
			break
			#6
		elif entry == '1':
			print("User has the ability to open programs")
		elif entry == '2':
			print("Admin has the abiliy to add and remove users")
		elif entry == '3':
			print("moderator has the ability to assign programs")
		elif entry == '4':
			print("permissions will be coming in the next release of the software")
		else:
			print("invalid entry, please try again")

def mainloop():
	loginvar = True
	#7
	while loginvar:
		print("A. Get roles\nB. list apps\nC. Log Off\nenter h for help")
		select = input("Please select an option: ")
		if select.lower() == "c":
			loginvar = False
		#8
		elif select.lower() == "b":
			listapps()
			#9
		elif select.lower() == "a":
			getroles()
			#10
		elif select.lower() == 'h':
			print("A. Get roles\nB. list apps\nC. Log Off\nenter h for help")
		else:
			input("Please select a valid option: ")

