#Utilize conditional statements to guide program execution 
# based on user input regarding weather conditions

#Ask user to input currentt weather from predefined conditions
weather = input("What's the weather like today? (sunny/rainy/cold): ")

#Recommend different clothes depending on weather conditions
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")