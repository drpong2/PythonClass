#TIY8.3
import locations
#from locations import city_country

index={}

while len(index) < 3:
    a = input("Please enter a city: ")
    b = input("Please enter the country that city is in: ")
    tempval = locations.city_country(a, b)
    index.update(tempval)
# Had to use google to get the above
print(index)

#8-7 Album - make_album(artist, album)
#build dict describing album
# Use `none` to add optional parameter that allows you to store the number of songs on an album
#make one function call with number


value = locations.make_album(artist=input("please enter an artist name: "),album=input("Please enter an album title: "),songs=(input("Please enter the number of songs in the album. If you don't know, hit enter:")))
print(value)

#8-8 take 8-7 and use a while loop to take input before calling make_album

count = 0
while count < 2:
    value = locations.make_album(artist=input("please enter an artist name: "),album=input("Please enter an album title: "),songs=(input("Please enter the number of songs in the album. If you don't know, hit enter:")))
    print(value)
    count += 1


