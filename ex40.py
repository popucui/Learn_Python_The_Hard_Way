cities ={'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonvile'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
	if state in themap:
		return themap[state]
	else:
		return "Not found."
cities['_find'] = find_city

while True:
	print "State? (Enter to quit)",
	state = raw_input("> ")

	if not state: break

	city_found = find_city(cities, state)
	print city_found

# try using for loop
for city in cities:
	print city, cities[city]
