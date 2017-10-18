# European countries and their abbreviations
euCountries = {
    'Belgium': 'BE', 
    'Bulgaria': 'BG',
    'Denmark': 'DK',
    'Germany': 'DE'
}

# European capitals
euCities = {
    'BE': 'Brussels',
    'BG': 'Sofia',
    'DK': 'Copenhagen',
    'DE': 'Berlin'
}

# Adding more cities
euCities['DE'] = 'Koln'
euCities['DK'] = 'Kolding'

# printing out cities
print('-' * 10)
print('Germany has: ', euCities['DE'])
print('-' * 10)

# printing out euCountries, their capitals and then additional cities
print('-' * 10)
print('Germany\'s cities are: ', euCities[euCountries['Germany']] )
print('-' * 10)