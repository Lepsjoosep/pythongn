import random

x = random.randint(0, 100)
userinput = int(input("Arva mis numbri peale arvuti mõtleb, mis on 0 - 100:"))

while x != userinput:
    if x == userinput:
        print("Õige vastus, kõva mees oled")
    elif x > userinput:
        print("Number mille peale arvuti mõtleb on suurem kui sinu arv")
        userinput = int(input("Paku uuesti:"))
    elif x < userinput:
        print("sinu arv on suurem kui arv mille peale arvuti mõtleb")
        userinput = int(input("Paku uuesti:"))
    elif userinput > 101:
        print("veic liiga suur arv selle mängu jaoks")
        userinput = int(input("Paku väiksem arv:"))

if x == userinput:
    print("õige vastus")
