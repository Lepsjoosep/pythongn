def isik():
    nimi = str(input("Mis teie nimi on? "))
    print("Tervist " + nimi)
    vanus = float(input("Kui vana te olete? "))
    if vanus == 18:
        print("Palju õnne täiskasvanuks saamise puhul, " + nimi)
    if vanus >= 18:
        print("Sa saad täiega juua ilma mingi jamata muidu saad autot juhtida")
    if vanus <= 18:
        print("Sa oled alakas :D, sa liiga noor, et LEGAALSELT autot juhtida muidu poh")
    elukoht = str(input("Kus teie elukoht asub? "))
    if elukoht == "saaremaa" or "Saaremaa":
        print("Väga lahe elad " + elukoht) 

isik()