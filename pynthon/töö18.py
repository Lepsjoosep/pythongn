import random


mang = ['paber', 'käärid', 'kivi']
x = 0

valik = random.choice(mang)
userinput = input("kivi, paber või käärid:")

if userinput == valik:
    print("viik")
elif userinput == "käärid" and valik == "paber":
    print("Sa võitsid")
elif userinput == "kivi" and valik == "käärid":
    print("Sa võitsid")
elif userinput == "käärid" and valik == "kivi":
    print("said lutti")
elif userinput == "paber" and valik == "käärid":
    print("said lutti")
elif userinput == "paber" and valik == "kivi":
    print("sa võitsid")
elif userinput == "kivi" and  valik == "paber":
    print("said lutti")
