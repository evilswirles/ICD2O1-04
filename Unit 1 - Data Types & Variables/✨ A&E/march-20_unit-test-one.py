#ask user for dimensions
length = float(input("Enter the length of the aquarium (cm): "))
width = float(input("Enter the width of the aquarium (cm): "))
height = float(input("Enter the height of the aquarium (cm): "))

#surface area calculations
surface_area = 2 * ((length * width) + (length * height) + (width * height))

#cost of glass per square cm
glass_cost_per_cm2 = 0.15

#total cost calculated
total_cost = surface_area * glass_cost_per_cm2

print(f"Total surface area: {surface_area:.2f} cm²") #total surface area
print(f"Total cost of the glass: ${total_cost:.2f}") #total cost of the glass
