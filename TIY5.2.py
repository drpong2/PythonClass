#TIY5.2 - 
import random

#5-3 Alien colors #1
colors= ["green", "yellow", "red"]
aliencolor=random.choice(colors)
print(aliencolor)
if "green" in aliencolor:
    print("Congratulations player! You earned 5 points!")
# write a version that fails

#5-4 Alien colors 2
#Choose a color for an alien as in 5-3, and write an if-else chain
#5 points for green, 10 points for not green
colors= ["green", "yellow", "red"]
aliencolor=random.choice(colors)
print(aliencolor)
if "green" in aliencolor:
    print("Congratulations player! You earned 5 points!")
else:
    print("10 points")

# one version with if, one version with else
colors= ["green", "yellow", "red"]
aliencolor="green"
print(aliencolor)
if "green" in aliencolor:
    print("Congratulations player! You earned 5 points!")
else:
    print("10 points")
#else
colors= ["green", "yellow", "red"]
aliencolor="red"
print(aliencolor)
if "green" in aliencolor:
    print("Congratulations player! You earned 5 points!")
else:
    print("10 points")


#5-5 Alien colors 3
#Turn your if-else chain from 5-4 into an if-elif-else chain
#5-10-15 green-yellow-red
# 3 versions of the program?
colors= ["green", "yellow", "red"]
aliencolor=random.choice(colors)
print(aliencolor)
if aliencolor == "green":
    print("Congratulations player! You earned 5 points!")
elif aliencolor == "yellow":
    print("10 points")
else:
    print("15 points")


#5-6 Stages of Life: write an if-elif-else chain that determines a person's stage of life. Set a values
# < 2 baby, 2 < 4 toddler, 4<13, kid, 13<20 teen, 20<65 adult, 65+ elder
possibleages = range(1,70)
agelist=[]
for number in range(1,11):
    agelist.append(random.choice(possibleages))
agelist.append(2)
agelist.append(4)
agelist.append(13)
agelist.append(20)
agelist.append(-2)
agelist.append("Steve")
for age in agelist:
    if age <= 2:
        print("just a baby")
    elif 2 < age <= 4:
        print(f"Learning to walk, moving around ({age})")
    elif 4 < age <= 13:
        print(f"You think you know everything, but you're just a kid({age})")
    elif 13 < age <= 20:
        print(f"annoying ({age})")
    elif 20 < age <= 65:
        print(f"Enjoy your taxes, loser ({age})")
    elif age > 65:
        print(f"Just like being a kid again, only hopefully this time with a house ({age})")
    elif age < 0:
        print("Please enter a positive number")
    else:
        print("Please enter a number")
        

#5-7 favorite fruit
#make a list of 3 favorite fruits then write a series of independent if statements that check for certain fruits in your list
#favorite_fruits
#5 if statements for fruit