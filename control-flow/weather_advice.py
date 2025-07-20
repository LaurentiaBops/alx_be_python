#Utilize conditional statements to guide program execution 
# based on user input regarding weather conditions

#Ask user to input currentt weather from predefined conditions
weather_conditions = str(input("What's the weather like today? (sunny/rainy/cold): ")).lower()

#Recommend different clothes depending on weather conditions
if weather_conditions == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather_conditions == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather_conditions == "cold":
    print("Make sure to wear a warm coat and scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")