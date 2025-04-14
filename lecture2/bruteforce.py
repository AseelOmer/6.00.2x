from itertools import chain, combinations

class Item:
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight

    def get_value(self):
        return self.value

    def get_weight(self):
        return self.weight

    def __str__(self):
        return f"{self.name}: <Value: {self.value}, Weight: {self.weight}>"

def build_items():
    names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'coke', 'apple', 'donut']
    values = [89, 90, 30, 50, 90, 79, 90, 10]
    weights = [123, 154, 258, 354, 365, 150, 95, 195]
    return [Item(n, v, w) for n, v, w in zip(names, values, weights)]

def powerset(items):
    # Generate all subsets (the power set)
    return chain.from_iterable(combinations(items, r) for r in range(len(items)+1))

def brute_force_knapsack(items, max_weight):
    best_value = 0
    best_subset = None
    for subset in powerset(items):
        total_weight = sum(item.get_weight() for item in subset)
        total_value = sum(item.get_value() for item in subset)
        if total_weight <= max_weight and total_value > best_value:
            best_value = total_value
            best_subset = subset
    return best_value, best_subset

def main():
    items = build_items()
    max_weight = 750
    val, taken = brute_force_knapsack(items, max_weight)
    print(f"\n[Brute Force] Total value = {val}")
    for item in taken:
        print(f"  {item}")

if __name__ == "__main__":
    main()