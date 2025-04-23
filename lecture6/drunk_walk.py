import random
import math
import matplotlib.pyplot as plt

# --- Location class ---
class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        return Location(self.x + dx, self.y + dy)

    def get_coords(self):
        return (self.x, self.y)

    def distance_from(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.hypot(dx, dy)

# --- Field class ---
class Field:
    def __init__(self):
        self.drunks = {}

    def add_drunk(self, drunk, loc):
        self.drunks[drunk] = loc

    def move_drunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError("Drunk not in field")
        x_dist, y_dist = drunk.take_step()
        current_location = self.drunks[drunk]
        self.drunks[drunk] = current_location.move(x_dist, y_dist)

    def get_loc(self, drunk):
        return self.drunks[drunk]

# --- Drunk base class ---
class Drunk:
    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        return "Anonymous Drunk" if self.name is None else self.name

# --- UsualDrunk ---
class UsualDrunk(Drunk):
    def take_step(self):
        step_choices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(step_choices)

# --- ColdDrunk ---
class ColdDrunk(Drunk):
    def take_step(self):
        step_choices = [(0.0, 0.9), (0.0, -1.03), (1.03, 0.0), (-0.9, 0.0)]
        return random.choice(step_choices)

# --- Walk and plot function ---
def walk_and_plot(field_class, drunk_class, steps=100):
    drunk = drunk_class()
    field = field_class()
    origin = Location(0, 0)
    field.add_drunk(drunk, origin)
    locations = [origin.get_coords()]

    for _ in range(steps):
        field.move_drunk(drunk)
        loc = field.get_loc(drunk)
        locations.append(loc.get_coords())

    # Plotting
    xs, ys = zip(*locations)
    plt.plot(xs, ys, label=drunk_class.__name__)
    plt.scatter(xs[0], ys[0], color='green', label='Start')
    plt.scatter(xs[-1], ys[-1], color='red', label='End')
    plt.title(f"{drunk_class.__name__} Walk ({steps} steps)")
    plt.xlabel('X position')
    plt.ylabel('Y position')
    plt.legend()
    plt.axis('equal')
    plt.grid(True)
    plt.show()

# --- Run the simulation ---
walk_and_plot(Field, UsualDrunk, steps=100)
walk_and_plot(Field, ColdDrunk, steps=100)