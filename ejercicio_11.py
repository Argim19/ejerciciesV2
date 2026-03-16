print("products:")
print("1. cono  = 3000")
print("2. vaso  = 4000")
print("3. banana split  = 9000")
 
cono = 0
vaso = 0
banana_split = 0
total = 0
count = ""
client = 1

while True:
    print("")   
    print("client",client)
    product = input("enter the product:")

    if product == "exit":
        break

    quantity = int(input("enter the quantity:"))
    
    if product == "cono":
        total += quantity * 3000
        cono += quantity
    elif product == "vaso":
        total += quantity * 4000
        vaso += quantity
    elif product == "banana split":
        total += quantity * 9000
        banana_split += quantity
    else:
      print("error")
      continue

    client += 1

if cono > vaso and cono > banana_split:
    count = "cono"

elif vaso > cono and vaso > banana_split:
    count = "vaso"

elif banana_split > cono and banana_split > vaso:
    count = "banana split"        

print("")
print("TOTAL VENDIDO:",total)
print("")   
print("CLIENTES ATENDIDOS:",client - 1) 
print("")   
print("PRODUCTO MAS VENDIDO:",count)      
