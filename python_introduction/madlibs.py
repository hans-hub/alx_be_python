#prompt users for inputs
adjective1= input("Enter your adjective (sunny,rainy): ")
adjective2= input("Enter your adjective2 (silly,sleepy): ")
adjective3= input("Enter your adjective3(majestic,grumpy): ")
adjective4= input("Enter your adjective4 (wild,boring): ")

#adding the story
story = f"On a beautiful {adjective1} day, I went to the Zoo. "
story += f"I saw a funny {adjective2} monkey swinging from the trees."
story += f"Then, I spotted a {adjective3} lion lounging in the sun. "

#conditional twist 
if adjective4 == "boring":
    story += "Honestly, it felt like watching paint dry. "
elif adjective4 == "exciting":
    story += "It was so thrilling, I almost screamed!!"
else:
    story += f"what a wild and {adjective4} experience!!!"

print(story)