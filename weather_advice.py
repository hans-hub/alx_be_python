weather = input("What's the weather like(sunny/rainy/cold): ").lower()

if weather == "rainy":
    print("Don't forget your umbrella and a raincoat")
elif weather == "sunny":
    print("Wear a t-shirt and sunglasses")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf")
else:
    print("Sorr, I dont have recommendations for this weather")