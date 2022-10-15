fav_foods = ['Pizza', 'Tacos', 'Salmon']
fav_foods = tuple(fav_foods)

# for food in fav_foods:
    # if food == "Pizza":
    #     size = input("What size pizza would you like?")
    #     print(f"You ordered a {size} pizza")
    # print(food)

# food = "Pizza!"
# for letter in food:
#     print(letter)

#dictionary for loops
person = {
    "nama": "Gilang",
    "twitter": "@g_r12",
    "instagram": "@12rgilang"
}
#can accesing key and valeu in dictionary loops
for key, value in person.items():
    print(f"The key is {key} and the value is {value}")
