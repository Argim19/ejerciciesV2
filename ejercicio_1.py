vainilla = 0
chocolate = 0
fresa = 0

for i in range(5):
   dato = input("elija un sabor enre vainilla, chocolate, fresa: ")
   if dato == "vainilla":
      vainilla +=1
   elif dato == "chocolate":
      chocolate +=1
   elif dato == "fresa":
      fresa +=1
   else:
      print("elija un sabor correcto")      
    
print("vainilla:",vainilla)
print("chocolate:",chocolate)
print("fresas:",fresa)
