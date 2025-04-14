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

def greedy(items, max_weight, key_function):
    items_copy = sorted(items, key=key_function, reverse=True)
    result = []
    total_value, total_weight = 0.0, 0.0
    for item in items_copy:
        if (total_weight + item.get_weight()) <= max_weight:
            result.append(item)
            total_weight += item.get_weight()
            total_value += item.get_value()
    return result, total_value

def test_greedy(items, constraint, key_function):
    taken, val = greedy(items, constraint, key_function)
    print(f"Total value of items taken = {val}")
    for item in taken:
        print(f"  {item}")

def main():
    items = build_items()
    max_weight = 750
    print("Greedy by value:")
    test_greedy(items, max_weight, lambda x: x.get_value())
    print("\nGreedy by weight:")
    test_greedy(items, max_weight, lambda x: 1 / x.get_weight())
    print("\nGreedy by value/weight ratio:")
    test_greedy(items, max_weight, lambda x: x.get_value() / x.get_weight())

if __name__ == "__main__":
    main()
