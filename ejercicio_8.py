count = 0
for i in range(6):
    dato = int(input("enter the price:"))
    if dato > 100000:
        count += 1
print("products that cost more than 100000:", count)        