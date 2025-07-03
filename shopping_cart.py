#create a shopping cart programme that will continuosly ask the user for aa food product and the price of that product
#have an exit clause if the user wishes to stop addind more things to their cart
#at the end sho the food items and the total cost to the user

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy or press q to quit: ")
    if food.lower() == 'q':
        break
    else:
        price = float(input("enter price of the {food}: R"))
        foods.append(food)
        prices.append(price)
        
print(".......YOUR CART.......")

for food in foods:
    print(food)
    
for price in prices:
    total += price
    
    print(f"your total is: R{total}")