def greedy_cow_transport(cows, limit):
    trips = []  # List to store the trips
    cows_copy = cows.copy()  # Make a copy of the cows dictionary to avoid mutation
    while len(cows_copy) > 0:
        trip = []  # List to store cows for this trip
        remaining_space = limit  # Space left on the spaceship
        # Sort cows by weight in descending order (heaviest first)
        sorted_cows = sorted(cows_copy.items(), key=lambda x: x[1], reverse=True)
        
        for cow, weight in sorted_cows:
            if weight <= remaining_space:  # Check if the cow can fit
                trip.append(cow)  # Add the cow to the trip
                remaining_space -= weight  # Decrease the remaining space
                del cows_copy[cow]  # Remove the cow from the copy of cows

        trips.append(trip)  # Add the trip to the list of trips
    return trips
