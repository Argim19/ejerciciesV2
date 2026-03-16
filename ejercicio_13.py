total_day = 0

while True:
    print("products:")
    print("coffe = 4000")
    print("cappuccino = 7000")
    print("cake = 6000")

    product = input("select a product:")
    
    if product == "exit":
        break

    if product == "coffe":
        price = 4000
    elif product == "cappuccino":
        price = 7000
    elif product == "cake":
        price = 6000
    else:
        print("invalid product")
        continue 


    quantity = int(input("enter the quantity:"))
    total = quantity * price

    if total > 20000:
        discount = total * 0.10
        total = total - discount
        print("10% discount applied")

    print("total for this customer:",total)
    total_day += total

print("total saless for the day:", total_day)                 