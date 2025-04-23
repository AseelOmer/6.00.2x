import random

# Set number of simulations
num_tests = 100000
boxcars = 0

for i in range(num_tests):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    if die1 == 6 and die2 == 6:
        boxcars += 1

# Estimate the probability
estimated_probability = boxcars / num_tests

print("Estimated probability of rolling boxcars:", estimated_probability)
