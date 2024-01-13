# Defining a function to calculate the dicounted price
def calculate_discount(original_price, discount_percentage):
    discount_amount = (discount_percentage / 100) * original_price
    discounted_price = original_price - discount_amount
    return discounted_price

# Prompting the user for price
original_price = int(input("Enter the original price in $: "))
discount_percentage = 15
final_price = calculate_discount(original_price, discount_percentage)

# Decision making
if (final_price < 50):
    print("Low-cost item.")
elif (final_price >= 50 and final_price <= 100):
    print("Moderate-cost item.")
else:
    print("High-cost item.")