child = 0
adult = 0
senior = 0
total_people = 0


capacity = int(input("enter the room capacity:"))

while total_people < capacity:
    age = int(input("enter the age:"))
    if age < 18:
        print("child")
        child += 1
        
    elif age <= 60:
        print("adult")
        adult += 1
    else:
        print("senior")
        senior += 1
    total_people += 1
    date = input("continue? s/n:")
    if date == "n":
        break
    else:
        continue


print("total number of people admitted:", total_people)
print("child:", child)
print("adult:", adult)
print("senior:", senior)

if total_people == capacity:
    print("the room was full")
else:
    print("The room wasn't full")    

    