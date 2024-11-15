#9-13 - dice using random, method called roll_die()
#make a 6-sided die and roll it 10 times

#I got carried away...
from random import choice as c
'''
class Die:
	def __init__(self,sides = 4):
		self.sides = sides
		self.diesides = range(1,sides)
		self.rolls = 0
		self.rolllist = []
		
	def roll_die(self,rolls=1):
		if rolls > 1:
			dierolls = range(1,rolls)
			for dieroll in dierolls:
				self.rolllist.append(dieroll)
		else:
			self.rolls = 1
			dierolls = 1
		print(f"roll list: {self.rolllist}")
		print(dierolls)
		for roll in dierolls:
			print(c(self.diesides))
			
d6 = Die(6)
print(f"Die 1 has {d6.sides} sides")
d20 = Die(20)
print(f"Die 2 has {d20.sides} sides")
print(f"rolling the {d6.sides}-sided die {d6.rolls} times:")
d6.roll_die(1)

dierolls =[]
for num in range(1,1):
	dierolls.append(num)
print(dierolls)
print(c(dierolls))
i = 0
while i < 10:
	print(c(dierolls))
	i += 1

#d20.roll_die(10)


class Die:
	def __init__(self,sides = 4):
		self.sides = sides
		self.diesides = range(1,sides)

	def roll_die(self,rolls=1):
		self.rolls = rolls
		current_roll = 0
		while current_roll < self.rolls:
			print(c(self.diesides))
			current_roll += 1

mydie = Die(6)
mydie.roll_die(2)
d20 = Die(20)
d20.roll_die(10)
		
'''	
#9-14 - Lottery - list or tuple containing a series of 10 numbers and 5
# letters. Randomly select 4 numbers or letters from the list. Print msg
# saying any ticket matching is a winner

lottery_list = []
hexlist = []
for num in range(1,16):
	lottery_list.append(num)
print(lottery_list)
for num in lottery_list:
	hexlist.append(hex(num).strip('0x'))
hexlist.append('0')
	
print(hexlist)
randomlist = [c(hexlist)]
randomlist.append(c(hexlist))
randomlist.append(c(hexlist))
randomlist.append(c(hexlist))
print(randomlist)


#9-15 - Lottery Analysis - Write a loop to win the previous number
#print a message noting how many times the loop had to run
def lotto_ticket():
	ticket = [c(hexlist)]
	ticket.append(c(hexlist))
	ticket.append(c(hexlist))
	ticket.append(c(hexlist))
	print(ticket)
	return ticket
	
dollarspent = 0
#buyticket = randomlist
buyticket = lotto_ticket()
print(buyticket)
print(f'your ticket: {buyticket}\nnext line')
print(randomlist)
gamble = True

while gamble:
	if buyticket == randomlist:
		string_literal = f"Your ticket: {buyticket}\nThe winning ticket: {randomlist}\nDollars spent: {dollarspent}"
		print(string_literal)
		gamble = False
	else:
		buyticket = lotto_ticket()
		dollarspent += 1
		if dollarspent % 1000 == 0:
			print(f"Your ticket: {buyticket}\nThe winning ticket: {randomlist}\nDollars spent: {dollarspent}")

'''
while buyticket != randomlist:
	buyticket = lotto_ticket
	dollarspent += 1
	if dollarspent % 100:
		#buyticket = randomlist
		print(f"Your ticket: {buyticket}\nThe winning ticket: {randomlist}\nDollars spent: {dollarspent}")
print(f"You spent ${dollarspent} trying to win the lottery")
'''

#9-16 - Python Module of the week
#pymotu - random
