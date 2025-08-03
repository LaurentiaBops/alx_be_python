# Convert temperatures between Celsius and Fahrenheit

#Define global variables to store conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

#Function that takes a temperature in Fahrenheit and converts
#to Celsius
def convert_to_celsius(fahrenheit):
    celcuis = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {celcuis}°C")

#Function that takes a temperature in Celsius and converts
#to Fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    print(f"{celsius}°C is {fahrenheit}°F")


#Prompt user to enter the temperature
temperature = float(input("Enter the temperature to convert: "))
temp_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if temp_unit == "C":
    convert_to_fahrenheit(temperature)
elif temp_unit == "F":
    convert_to_celsius(temperature)
else:
    print("Invalid temperature. Please enter a numeric value.")
   
