# Function to calculate tax and return the total
def calculate_tax(price, tax_rate):
    total = price + (price*tax_rate)
    return total        # Return the total


my_price = float(input("Enter a price: "))

# Call the function and store the result in total_price
total_price = calculate_tax(my_price, 0.06)

print("price = ", my_price, " Total price = ", total_price)
