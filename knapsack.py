import collections

LOAD_CAPACITY = 400
DATA = [
    ('map', 9, 150),
    ('compass', 13, 35),
    ('water', 153, 200),
    ('sandwich', 50, 160),
    ('glucose', 15, 60),
    ('tin', 68, 45),
    ('banana', 27, 60),
    ('apple', 39, 40),
    ('cheese', 23, 30),
    ('beer', 52, 10),
    ('suntan cream', 11, 70),
    ('camera', 32, 30),
    ('T-shirt', 24, 15),
    ('trousers', 48, 10),
    ('umbrella', 73, 40),
    ('waterproof trousers', 42, 70),
    ('waterproof overclothes', 43, 75),
    ('note-case', 22, 80),
    ('sunglasses', 7, 20),
    ('towel', 18, 12),
    ('socks', 4, 50),
    ('book', 30, 10),
]

Item = collections.namedtuple('Item', 'name effectivity weight value')

ITEMS = [
    Item(name, value / weight, weight, value) for name, value, weight in DATA
]


class Knapsack:
    def __init__(self, load_capacity):
        self.free_space = load_capacity
        self.items = []

    def load(self, items):
        items.sort(key=lambda i: i.effectivity, reverse=True)
        trash = []
        for item in items:
            if item.weight <= self.free_space:
                self.load_item(item)
            else:
                trash.append(item)
        return trash

    def load_item(self, item):
        self.items.append(item)
        self.free_space -= item.weight


if __name__ == '__main__':
    from pprint import pprint
    knapsack = Knapsack(LOAD_CAPACITY)
    trash = knapsack.load(ITEMS)
    print('knapsack:')
    pprint(knapsack.items)
    print('trash:')
    pprint(trash)
    print(
        'total value in knapsack: {}'.format(
            sum(x.value for x in knapsack.items)
        )
    )
