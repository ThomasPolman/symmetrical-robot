# Gepersonaliseerd bezienswaardigheden algoritme voor reisbureau

destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "So Paulo, Brazil", "Cairo, Egypt"]

#Indexlocatie bestemming
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

#Vinden bestemmingsstring
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

#Koppeling bestemming met attracties
attractions = [[] for destination in destinations]

def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index (destination)
  except ValueError:
   	print("Gotcha!")
  attractions_for_destination = attractions[destination_index]
  attractions_for_destination.append(attraction)
  return attractions_for_destination

#Attracties
add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("So Paulo, Brazil", ["So Paulo Zoo", ["zoo"]])
add_attraction("So Paulo, Brazil", ["Ptio do Colgio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

#Koppeling attracties aan interesses
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for possible_attraction in attractions_in_city:
    attraction_tags = possible_attraction[1]
    
    for interest in interests:
        if interest in attraction_tags:
            attractions_with_interest.append(possible_attraction[0])        
  return attractions_with_interest

#Interface output aan de specifieke reiziger
def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": "
    for attr in traveler_attractions:
        interests_string += attr
    return interests_string

print(get_attractions_for_traveler(["Roland van der Heijden", "Paris, France", ["monument"]]))
