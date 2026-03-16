price = 0

print("coffee: 4000")
print("tea: 3500")
print("juice: 5000")

drink = input("what drink do you want?:")
quantity = int(input("enter the quantity:"))
if drink == "coffee":
    price = quantity * 4000
elif drink == "tea":
    price = quantity * 3500
elif drink == "juice":
    price = quantity * 5000
else:
    print("enter one of the available drinks")    

print("the total to pay is:",price)  
    

