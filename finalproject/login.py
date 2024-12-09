import passwordplain

def auth():
	print('='*28)
	print('=',' '*24,'=')
	print("=   CLASS LOGIN AND MENU   =")
	print('=',' '*24,'=')
	print('='*28)

	userpick = ''
	#1
	while userpick.lower() != 'q':
		print("press 1 to login, 2 to create a login, 'q' to quit: ")
		userpick = input()
		#2
		if userpick.lower() == 'q':
			quit()
			#3
		elif userpick.lower() == '1':
			passwordplain.uservalidate()
			#4
		elif userpick.lower() == '2':
			passwordplain.newuser()
			#5
		else:
			print("please select a valid option")
	
passwordplain.loadusers()
#6

auth()
#7
