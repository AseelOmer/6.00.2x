import random
import math
from location import Location
from field import Field
from drunk import UsualDrunk, ColdDrunk

# -----------------------------
# Simulate a single walk
# -----------------------------
def walk(field, drunk, num_steps):
    """
    Move the drunk around the field for num_steps, and return the distance from the start.
    """
    start = field.get_loc(drunk)  # Where the drunk starts
    for _ in range(num_steps):
        field.move_drunk(drunk)   # Move the drunk one step
    end = field.get_loc(drunk)    # Where the drunk ends
    return start.dist_from(end)   # Calculate distance from start to end


# -----------------------------
# Simulate multiple walks
# -----------------------------
def sim_walks(num_steps, num_trials, d_class):
    """
    Run num_trials walks for a drunk of type d_class, each with num_steps steps.
    Returns list of distances.
    """
    homer = d_class("Homer")      # Create a drunk of the specified class
    origin = Location(0, 0)       # Start point
    distances = []
    for _ in range(num_trials):
        field = Field()           # New field each time
        field.add_drunk(homer, origin)
        distance = walk(field, homer, num_steps)
        distances.append(round(distance, 1))
    return distances


# -----------------------------
# Run tests for one drunk type
# -----------------------------
def drunk_test(walk_lengths, num_trials, d_class):
    """
    Run multiple walks of varying lengths and print results.
    """
    for num_steps in walk_lengths:
        distances = sim_walks(num_steps, num_trials, d_class)
        mean = round(sum(distances) / len(distances), 4)
        max_dist = max(distances)
        min_dist = min(distances)
        print(f"{d_class.__name__} random walk of {num_steps} steps:")
        print(f"  Mean = {mean}, Max = {max_dist}, Min = {min_dist}\n")


# -----------------------------
# Compare multiple drunk types
# -----------------------------
def sim_all(drunk_types, walk_lengths, num_trials):
    """
    Run drunk_test for multiple types of drunks.
    """
    for d_class in drunk_types:
        drunk_test(walk_lengths, num_trials, d_class)


# -----------------------------
# Run the final experiment
# -----------------------------
random.seed(0)  # Make results reproducible

walk_lengths = [10, 100, 1000, 10000]
num_trials = 100

# Run simulation for both UsualDrunk and ColdDrunk
sim_all((UsualDrunk, ColdDrunk), walk_lengths, num_trials)
