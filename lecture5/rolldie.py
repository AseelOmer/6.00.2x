import random

goal = [1, 1, 1, 1, 1]
num_trials = 1000
total = 0

for i in range(num_trials):
    roll = [random.randint(1, 6) for _ in range(len(goal))]
    if roll == goal:
        total += 1

print("Estimated probability:", total / num_trials)
