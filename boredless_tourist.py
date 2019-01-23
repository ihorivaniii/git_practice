destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "So Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wikes', 'Shanghai, China', ['historical site', 'art']]


def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index


def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index


test_destination_index = get_traveler_location(test_traveler)

attractions = []
for destination in destinations:
    attractions.append([])


def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
        attractions_for_destination = attractions[destination_index].append(attraction)
    except ValueError:
        return
        print("error of value")


add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscarper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("So Paulo, Brazil", ["So Paulo Zoo", ["zoo"]])
add_attraction("So Paulo, Brazil", ["Ptio do Colgio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Piramids of Giza", ["monument", "historical site"]])
add_attraction("Cario, Egypt", ["Egyptian Museum", ["museum"]])


def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []

    for attraction in attractions_in_city:
        possible_attraction = attraction
        attractions_tags = attraction[1]
        for interest in interests:
            if interest in attractions_tags:
                attractions_with_interest.append(possible_attraction[0])
    return attractions_with_interest


def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    interests_string = "Hi " + traveler[0] + ", we think you'll like these place around " + traveler_destination + ": "
    for i in range(len(traveler_attractions)):
        if traveler_attractions[-1] == traveler_attractions[i]:
            interests_string += "the " + traveler_attractions[i] + "."
        else:
            interests_string += "the " + traveler + attractions[i] + ", "
    return interests_string


smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)

