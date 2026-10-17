#LIST
prices = [100, 200, 300, 400, 500]

print(prices[0]) #first
print(prices[-1]) #last
print(prices[1:4]) #2 to 3
print(prices[:3]) #all upto 3
print(prices[::2]) #every 2nd item

#TUPLES and SETS
point = (10,20) # is a touple
unique = {1,2,2,3} # is a set
print(point)
print(unique)

#DICTIONARY
product = {
    "name": "Ring",
    "price": 50000,
    "stock": 5
}

print(product["price"])
product["stock"] = 4
product['metal'] = 'gold'

for key, value in product.items():
    print(key, "->", value)

#DICTIONARIES AS A LIST
sales = [
    {"item": "Ring", "amount": 5000},
    {"item": "Necklace", "amount": 10000}
]

