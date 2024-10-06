#TIY4.2
'''
#4-3 Count to 20
numbers = list(range(1,21))
print(numbers)

#4-4 - one million
millions= list(range(1,1000001))

for number in millions:
    print(number)
  

#4-5 sumillion
print(min(millions))
print(max(millions))
print(sum(millions))


#4-6 Odd Numbers
oddities = list(range(1,21,2))
for number in oddities:
    print(number)

#4-7 Threes
threes = list(range(3,31,3))
for number in threes:
    print(number)

#4-8 Cubes
base=list(range(1,10))
powers=list()
for number in base:
    powers.append(number**3)
print(powers)
'''
#4-9 cube comprehension
powers = [value**3 for value in range(3,31,3)]
print(powers)
