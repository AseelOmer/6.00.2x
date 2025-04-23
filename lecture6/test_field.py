from field import Field
from drunk import UsualDrunk
from location import Location

# Create a field
f = Field()

# Create a drunk named Homer
homer = UsualDrunk('Homer')

# Add Homer at location (0, 0)
start = Location(0, 0)
f.addDrunk(homer, start)

# Show starting point
print(f"Start location: {f.getLoc(homer)}")

# Move Homer 5 steps
for step in range(5):
    f.moveDrunk(homer)
    print(f"After step {step + 1}: {f.getLoc(homer)}")

# Show distance from start
finalLoc = f.getLoc(homer)
distance = finalLoc.distFrom(start)
print(f"\nTotal distance from start: {distance:.2f}")
