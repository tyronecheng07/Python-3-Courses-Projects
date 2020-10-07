toppings = [
    'pepperoni',
    'pineapple',
    'cheese',
    'sausage',
    'olives',
    'anchovies',
   'mushrooms',
]

prices = [
    2,
    6,
    1,
    3,
    2,
    7,
    2,
]

num_pizzas = len(toppings)

print("We sell " + str(num_pizzas) + " different kinds of pizza!")

pizzas = list(zip(prices, toppings))

print(pizzas)

sorted_pizza = sorted(pizzas)

cheapest_pizza = sorted_pizza[0]

priciest_pizza = sorted_pizza[-1]

three_cheapest = sorted_pizza[:3]

print(three_cheapest)

num_two_dollar_slices = prices.count(2)

print(num_two_dollar_slices)

