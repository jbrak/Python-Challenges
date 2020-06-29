from random import randint

coin = ["heads","tails"]

while True:

    rand = randint(0,1)
    try:
        user = coin.index(input("Heads or Tails?\n").lower())
    except:
        print("Invalid choice\n")
        user = coin.index(input("Heads or Tails?\n").lower())

    if user == rand:
        print("You Win\n")
    elif user != rand:
        print("Bad Luck\n")

    if input("Do you want to try again? Y/N\n").upper() == "N":
        break
