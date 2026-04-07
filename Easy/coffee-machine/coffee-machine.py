water_per_coffee = 200
milk_per_coffee = 50
coffee_beans_per_coffee = 15


print("Write how many cups of coffee you will need:")
num_cups_of_coffee = int(input())

print(f"For {num_cups_of_coffee} cups of coffee you will need:")
print(f"{int(num_cups_of_coffee * water_per_coffee)} ml of water")
print(f"{int(num_cups_of_coffee * milk_per_coffee)} ml of milk")
print(f"{int(num_cups_of_coffee * coffee_beans_per_coffee)} g of coffee beans")
