import copy


class Portfolio:
    def __init__(self):
        self.holdings = {}
        self._holdings = {}

    # AAPL, MSFT...

    def buy(self, ticker: str, shares: int):
        self.holdings[ticker] = self.holdings.get(ticker, 0) + shares

    def sell(self, ticker: str, shares: int):
        numbers_shares = self.holdings.get(ticker, 0)

        if numbers_shares < shares:
            raise Exception("Tolik akcii nemas v portofoliu")

        self.holdings[ticker] = numbers_shares - shares

    def __iter__(self):
        print("Alokuji do fake holdings")
        self._holdings = copy.deepcopy(self.holdings)

        return self

    def __next__(self):
        if len(self._holdings.keys()) <= 0:
            raise StopIteration()

        current = self._holdings.popitem()

        return current


portfolio = Portfolio()
portfolio.buy("AAPL", 10)
portfolio.buy("MSFT", 5)
portfolio.buy("NVDA", 1)

for item in portfolio:
    print(item)

for item in portfolio:
    print(item)

print(portfolio.holdings)

# list_1 = [1, 2, 3]
# list_1.reverse()
# print(list_1)

# shallow copy

# list_2 = list_1.copy()
# list_2 = list_1[::]  # [start:stop:step]

# list_1.pop()

# print(len(list_1))
# print(len(list_2))

# people_1 = {
#         "name": "Tomas",
#         "age": 10,
#         "hobbies": ["sleeping"],
#     }
#
# # people_2 = people_1.copy()  # shallow copy
# people_2 = copy.deepcopy(people_1)  # deep copy
#
# # people_1["name"] = "Jozka"
# people_1["hobbies"].append("Reading")
#
# print(people_1)
# print(people_2)
