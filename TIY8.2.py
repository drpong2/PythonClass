#TIY8.2

#8-3 T-shirt - make_shirt(size, text)
#print summary
def make_shirt(size, text):
    print(f'making a size {size} shirt that says "{text}"')

make_shirt("L", "Living Large")
make_shirt(text="Living large, but explicitly defined",size="large")

#8-4 Large shirts - modify previous function so shirts are large by default with default message "I love Python"
def make_shirt(size='Large', text='I love Python'):
    print(f'making a size {size} shirt that says "{text}"')

make_shirt()
make_shirt("L", "Living Large")
make_shirt(text="Living large, but explicitly defined",size="large")

#8-5 Cities - describe_city(city, country) - print sentence {city} is in {country}
#default contry value
def describe_city(city, country='US'):
    print(f"{city.title()} is in {country}")

describe_city("orlando")
describe_city("joliet")
describe_city("London","Canada")
