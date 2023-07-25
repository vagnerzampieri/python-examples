all_states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {
    "kone": set(["id", "nv", "ut"]),
    "ktwo": set(["wa", "id", "mt"]),
    "kthree": set(["or", "nv", "ca"]),
    "kfour": set(["nv", "ut"]),
    "kfive": set(["ca", "az"]),
}

final_stations = set()

# 1. Loop until you have gone through each state
while all_states_needed:
    # 2. Find the best station for each state
    best_station = None
    # 3. Set of all the states covered by this station
    states_covered = set()

    # 4. Loop through each station
    for station, states in stations.items():
        # 5. Find the states covered by this station that have not been covered yet
        covered = all_states_needed & states
        # 6. If this station covers more states than the current best station
        if len(covered) > len(states_covered):
            # 7. Set this station as the new best station
            best_station = station
            # 8. Set the states covered by this station as the new states covered
            states_covered = covered

    # 9. Add this station to the final stations
    final_stations.add(best_station)
    # 10. Remove the states covered by this station from the states needed
    all_states_needed -= states_covered

print(final_stations)