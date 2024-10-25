def abc(a, b, c): 

    if (a >= b) and (a >= c): 
        largest = a 

    elif (b >= a) and (b >= c): 
        largest = b 
    else: 
        largest = c 
        
    return largest 


# Driven code 
a = input("Esimene arv: ")
b = input("Teine arv: ")
c = input("kolmas arv: ")

print(abc(a, b, c)) 


