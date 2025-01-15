import random

dealer = random.randint(1, 11)
player = random.randint(1, 11)

print("player has a", player)
print("dealer has a", dealer)


decision1 = input("Type h to hit, s to stand: ")
if decision1 == "h" or decision1 == "H":
    player = player + random.randint(1, 11)
    print("player has hit, player has a", player)
elif decision1 == "s" or decision1 == "S":
    print("player stands")
else:
    print("player has no brains")
        
dealerdecision1 = random.randint(1, 11)
dealer =  dealerdecision1 + dealer
print("Dealer has a", dealer)

if dealer == 21:
    print("dealer has won")
elif player == 21:
    print("player has won")

decision2 = input("Type h to hit, s to stand: ")
if decision2 == "h" or decision2 == "H":
    player = player + random.randint(1, 11)
    print("player has hit, player has a", player)
elif decision2 == "s" or decision2 == "S":
    print("player stands")
else:
    print("player has no brains")
        
dealerdecision2 = random.randint(1, 11)
dealer =  dealerdecision2 + dealer
print("Dealer has a", dealer)

if dealer == 21:
    print("dealer has won")
elif player == 21:
    print("player has won")
elif player <= 21:
    print("player has lost")
