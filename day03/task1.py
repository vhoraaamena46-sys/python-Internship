prices = [100, 250, 300, 150, 500, 700, 200, 350, 450, 600]

average = sum(prices) / len(prices)

above_average = [price for price in prices if price > average]+

print("Prices:", prices)
print("Average Price:", average)
print("Prices Above Average:", above_average)