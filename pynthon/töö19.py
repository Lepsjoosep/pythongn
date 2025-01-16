import random

dealer = random.randint(1, 10)
player = random.randint(1, 10)

print("♤♤♤♤♤♤♤♤♤♤♤♤♤ Welcome to ♤Blackjack game ♤♤♤♤♤♤♤♤♤♤♤♤♤♤")
print("♤The Dealer will hand out the cards when you are ready♤")

ready = input("Are you ready, press y if you are:")

if ready == "y" or ready == "Y":
    print("dealer has handed out the cards and put one down.")
else:
    print("you did something wrong.")

print("player has a", player)
print("dealer has a", dealer)


decision1 = input("Type h to hit, s to stand: ")
if decision1 == "h" or decision1 == "H":
    playersecondcard = random.randint(1, 11)
    playercards = player + playersecondcard
    print("player has hit, player has a", player, playersecondcard, "that is", playercards)
elif decision1 == "s" or decision1 == "S":
    print("player stands")
else:
    print("player has no brains")
        
dealersecondcard = random.randint(1, 10)
dealercards =  dealersecondcard + dealer
print("Dealer reveals his second card, he now has a" , dealersecondcard, dealer, "thats", dealercards)


decision1 = input("Type h to hit, s to stand: ")
if decision1 == "h" or decision1 == "H":
    playersthirdcard = random.randint(1, 11)
    playercards = playercards + playersthirdcard
    print("player has hit, player has a", player, playersecondcard, playersthirdcard, "that is", playercards)
elif decision1 == "s" or decision1 == "S":
    print("player stands")
else:
    print("player has no brains")
        
dealerthirdcard = random.randint(1, 11)
dealercards =  dealerthirdcard + dealercards
print("Dealer has a", dealer, dealersecondcard,   dealerthirdcard, "thats", dealercards )

if dealercards == 21:
    print("dealer has won")
    exit()  
elif playercards == 21:
    print("player has won")
    exit()
elif playercards > 21:
    print("player has lost")
    exit()
elif dealercards > 21:
    print("Dealer has busted all over the place")
    exit()


decision1 = input("Type h to hit, s to stand: ")
if decision1 == "h" or decision1 == "H":
    playersfourthcard = random.randint(1, 11)
    playercards = playercards + playersfourthcard
    print("player has hit, player has a", player, playersecondcard, playersthirdcard, playersfourthcard, "that is", playercards)
elif decision1 == "s" or decision1 == "S":
    print("player stands")
else:
    print("player has no brains")

if dealercards >= 17 or dealercards <= 17 and dealercards <= 21:
    dealerfourthcard = random.randint(1, 11)
    dealercards =  dealerfourthcard + dealercards
    print("Dealer has a", dealer,  dealersecondcard, dealerthirdcard, dealerfourthcard, "thats", dealercards )


if dealercards == 21:
    print("dealer has won")
    exit() 
elif playercards == 21:
    print("player has won")
    exit()
elif playercards > 21:
    print("player has lost")
    exit()
elif dealercards > 21:
    print("Dealer has busted all over the place")
    exit()

decision1 = input("Type h to hit, s to stand: ")
if decision1 == "h" or decision1 == "H":
    playersfifthcard = random.randint(1, 11)
    playercards = playercards + playersfifthcard
    print("player has hit, player has a", player, playersecondcard, playersthirdcard, playersfourthcard, playersfifthcard, "that is", playercards)
elif decision1 == "s" or decision1 == "S":
    print("player stands")
else:
    print("player has no brains")

if dealercards >= 17 or dealercards <= 17 and dealercards <= 21:
    dealerfifthcard = random.randint(1, 11)
    dealercards =  dealerfourthcard + dealercards
    print("Dealer has a", dealer,  dealersecondcard, dealerthirdcard, dealerfourthcard,  "thats", dealercards )


if dealercards == 21:
    print("dealer has won")
    exit() 
elif playercards == 21:
    print("player has won")
    exit()
elif playercards > 21:
    print("player has lost")
    exit()
elif dealercards > 21:
    print("Dealer has busted all over the place")
    exit()


