def liigaasta(aasta):  
  if((aasta % 400 == 0) or (aasta % 100 != 0) and (aasta  % 4 == 0)):   
    print("on on liigaasta");    
  else:  
    print ("ei ole liigaasta")  
aasta = int(input("Sisesta aasta:  "))  
liigaasta(aasta)    