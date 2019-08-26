# Define function calculate_tax
def calculate_tax(price, tax_rate):
    total = price + (price*tax_rate)
    global my_price             # global 지정하여   
    my_price = my_price + 200   # 에러 발생하지 않음    
    return total


# Main program calls the function
my_price = float(input("Enter a price: "))

total_price = calculate_tax(my_price, 0.06)
print("price = ", my_price, " Total price = ", total_price)
