price_car = 4000
price_motorcycle = 2000
cars = 0
motorcycle = 0
total_price = 0
price_1 = 0
price_2 = 0

for i in range(3):
    placa = input("enter the placa:")
    type = input("enter the type (car/motorcycle):")
    hours = int(input("Enter parking hours:"))
    if type == "car":
        price_1 += price_car * hours
        cars += 1
    elif type == "motorcycle":
        price_2 += price_motorcycle * hours
        motorcycle += 1
    else:
        print("enter a value correct")

    total_price = (price_1 + price_2)
        
print("")
print("total recaudado:", total_price)
print("cantidad de carros:", cars)
print("cantidad de motos:", motorcycle)


if price_1 > price_2:
    print("vehiculo que mas pago: cars")
elif price_1 < price_2:
    print("vehiculo que mas pago: motorcycle")

else:
    print("pagaron igual")    

