water_per_coffee = 200
milk_per_coffee = 50
coffee_beans_per_coffee = 15

print("Write how many ml of water the coffee machine has:")
water_available = float(input())
print("Write how many ml of milk the coffee machine has:")
milk_available = float(input())
print("Write how many grams of coffee beans the coffee machine has:")
coffee_available = float(input())
print("Write how many cups of coffee you will need:")
cups_of_coffee_needed = int(input())

max_coffee_per_water = int(water_available // water_per_coffee)
max_coffe_per_milk = int(milk_available // milk_per_coffee)
max_coffee_per_beans = int(coffee_available // coffee_beans_per_coffee)

max_cups_of_coffee = min(max_coffee_per_water, max_coffe_per_milk, max_coffee_per_beans)

if max_cups_of_coffee == cups_of_coffee_needed:
    print("Yes, I can make that amount of coffee")
elif max_cups_of_coffee > cups_of_coffee_needed:
    print(f"Yes, I can make that amount of coffee (and even {max_cups_of_coffee - cups_of_coffee_needed} more than that)")
else:
    print(f"No, I can make only {max_cups_of_coffee} cups of coffee")