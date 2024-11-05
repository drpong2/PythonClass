#TIY8.3

#8-6 city names - city_country() building a dict, call 3 times
def city_country(city, country):
    index = {city: country}
    return index


def make_album(artist, album, songs=None):
    if songs:    
        index = {album: artist, 'Songs in album': songs}
    else:
        index = {album: artist}
    return index

