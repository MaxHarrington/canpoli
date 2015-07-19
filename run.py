import parliament

def get_tallies(year):
    canada = parliament.Parliament("2008")

    seat_values = list(canada.get_party_seats("2008").values())

    seat_tallies = dict()

    for seats in seat_values:
        seat_tallies[seats] = 0

    for seats in seat_values:
        seat_tallies[seats] += 1

    print(seat_tallies)

get_tallies("2008")