###QUESTION 5C###
#gas mileage calculator
start_km = 23340
end_km = 23695
gallons = 14.1

#calculate MPG
distance_km = end_km - start_km
distance_miles = distance_km * 0.621371
mpg = distance_miles / gallons

print(f"Miles per gallon: {mpg:.2f}")
