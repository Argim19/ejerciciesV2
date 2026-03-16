edad = int(input("enter age:"))
if edad < 13:
    print("you cannot enter")
elif edad >= 13 and edad <=17:
    print("class juvenil")
elif edad > 18 and edad <60:
    print("class general")
else:
    print("class senior")        
