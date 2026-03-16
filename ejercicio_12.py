low = 0
medium = 0
high = 0

for i in range(5):
    name = input("enter the name:")
    days = int(input("days attended during the week:"))
    minute = int(input("average minutes trained per day:"))

    if days < 3:
        low += 1
    elif days <= 4:
        medium += 1
    elif days >= 5:
        high += 1
    else:
        print("error")    


print("low commitment:",low)
print("medium commitment:",medium)  
print("high commitment:",high)                  
