class Shop:
    def __init__(self, products: dict[str, int] = None):
        if products:
            self.products = products
        else:
            self.products = {}

    def __next__(self):
        pass

    def __iter__(self):
        return self


# class Cart:
#     def __init__(self):
#         self.items = []
#         self._items = []
#
#     def add_item(self, item):
#         self.items.append(item)
#
#     def remove_item(self, item):
#         self.items.remove(item)
#
#     def __iter__(self):
#         self._items = self.items.copy()
#
#         return self
#
#     def __next__(self):
#         if len(self._items) <= 0:
#             raise StopIteration
#
#         return self._items.pop(0)

class Cart:
    def __init__(self):
        self.items = []
        self._items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def print_data(self):
        # for item in self.items:
        #     yield item

        result = []

        for item in self.items:
            result.append(item)

        return []


cart = Cart()
cart.add_item("rohlik")
cart.add_item("rohlik")
cart.add_item("rohlik")
cart.add_item("rohlik")
cart.add_item("chleba")
cart.add_item("brambory")

for item in cart.print_data():
    print(item)


