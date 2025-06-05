###QUESTION 2###
#elif
MAX_TEMP = 80
MIN_TEMP = 60

temperature = float(input("What is the temperature of the Porridge? "))

if (temperature > MAX_TEMP):
    print("Porridge too hot")
elif (temperature < MIN_TEMP):
    print("Porridge too cold")
else:
    print("Just right :)")

#nested if
MAX_TEMP = 80
MIN_TEMP = 60

temperature = float(input("What is the temperature of the Porridge? "))

if (temperature > MAX_TEMP):
    print("Porridge too hot")
else:
    if (temperature < MIN_TEMP):
        print("Porridge too cold")
    else:
        print("Porridge just right - eat it all up.")
