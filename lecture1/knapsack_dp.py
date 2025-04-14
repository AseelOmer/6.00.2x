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

def dp_knapsack(items, max_weight):
    # memo is a dictionary to remember previous solutions
    memo = {}

    def helper(i, available_weight):
        if (i, available_weight) in memo:
            return memo[(i, available_weight)]
        elif i == 0:
            if items[i].get_weight() <= available_weight:
                result = (items[i].get_value(), [items[i]])
            else:
                result = (0, [])
        else:
            without_item = helper(i - 1, available_weight)
            if items[i].get_weight() > available_weight:
                result = without_item
            else:
                with_value, with_list = helper(i - 1, available_weight - items[i].get_weight())
                with_value += items[i].get_value()
                if with_value > without_item[0]:
                    result = (with_value, with_list + [items[i]])
                else:
                    result = without_item
        memo[(i, available_weight)] = result
        return result

    return helper(len(items) - 1, max_weight)

def main():
    items = build_items()
    max_weight = 750
    value, taken = dp_knapsack(items, max_weight)
    print(f"\nTotal value of items taken = {value}")
    for item in taken:
        print(f"  {item}")

if __name__ == "__main__":
    main()
