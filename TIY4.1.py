#ch4 TIY 1
'''
Looping - Looping through a list is very powerful
indents - subsections of code, like plusses in notepad++
 - Python tells you when it expects indents and there are none
 - Python tells you when there are unexpected indents
 - indents must be uniform
range function - Creates a list of numbers
    - you can do manipulations, it's not just straight numbers
Slicing a list - Before or after the colon, number determines where to start/how far to go
    players[1:4]
    players [-3:]
    Don't copy a list using list_a = list_b, as tpython assumes both variables are referencing the same list (p116)
'''
 


#p.105
#4-1 - Pizzas
pizzas=["sausage","pepperoni","meatlovers"]
for pizza in pizzas:
  print(f"I love {pizza}")
print("I love any kind of pizza, really")

#4-2 - animals
animals=["Dog","cat","elephant"]
answer=["would","would","would not"]
answerindex=0
for animal in animals:
  #print(answerindex)
  #print(answer[answerindex]
  print(f"a {animal} {answer[answerindex]} make a good pet")
  answerindex +=1
  print(answerindex)
  
print(f"you should definitely not own a {animals[-1]}")
demonstrationlist = animals[:]
animals.append("gecko")
answer.append("would")
answerindex=0
print(answer)
for animal in animals:
  #print(answerindex)
  #print(answer[answerindex]
  print(f"a {animal} {answer[answerindex]} make a good pet")
  answerindex +=1
  print(answerindex)
print(demonstrationlist)
