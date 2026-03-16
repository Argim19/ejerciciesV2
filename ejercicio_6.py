time = int(input("enter the numbers of hours"))
if time == 1:
    print("total to pay:",5000)
else:
    print("total to pay:", 5000 + (time - 1) * 3000)    