numbrid = [1, 2, 3, 4, 5]
for x in numbrid:
    print(x)
    if x == 5:
        break

numbrid2 = [5 ,4 ,3 ,2 ,1]
for y in numbrid2:
    print(y)
    if y == 1:
        break

def Check_vows(string, tähed):
    final = [each for each in string if each in tähed]
    print(len(final))
    print(final)

string = "Vetsus on rahvast rohkem kui inimesi"
tähed   = "aeiouõäöüAEIOUÕÄÖÜ"
Check_vows(string, tähed)
