# age = input("What is your age? ")
# dog_years = int(age) * 7
# print(dog_years)

# name = input("What is your name? ")
# print("Hello,", name)

# introduction = input("hello everyone, my name is gilang where are you from? ")
# print("We are from", introduction)

# Game Rock, Papper, Scicors

game = input("we are going to play Rock Papper Scicors, lets play the game.. (type ypur choose)")
lst = ["Rock", "Papper", "Scicors"]
if game == "Rock":
    print("you're Choosing", game, "im choosing",lst[1])
elif game == "Papper": 
    print("you're Choosing", game, "im choosing",lst[2])
elif game == "Scicors":
    print("you're Choosing", game, "im choosing",lst[0])
