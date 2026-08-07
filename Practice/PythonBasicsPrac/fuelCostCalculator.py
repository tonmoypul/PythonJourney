#Distance in kilometer
distance = 347 

#Mileage == how far a vehicle can travel on a specific amount of fuel, measured in kilometers per liter (km/l)
mileage = 40

#Fuel Price per liter
fuelPrice = 145

fuelRequirement = distance / mileage
fuelCost = fuelRequirement * fuelPrice

print(f"Required fuel: {fuelRequirement:.2f} liters\nFuel Price: {fuelPrice:.2f} Tk per liter\nTotal price: {fuelCost:.2f} Tk.")
