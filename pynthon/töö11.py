puuviljad = ["Arbuus", "Õun", "Virsik"]
print(puuviljad)

if "Õun" in puuviljad:
    print("Õun on listis")
else:
    print("Õun ei ole listis")

puuviljad.remove("Arbuus")
print(puuviljad)

print("Virsik")

puuviljad[0] = "Melon"
print(puuviljad)

if "Õun" in puuviljad:
    print("Õun on listis")
else:
    print("Õun ei ole listis")

print(len(puuviljad))   


