time = int(input("Enter your arrival time (0 to 23):"))
if time >= 6 and time <= 11:
    print("morning")
elif time >= 12 and time <= 17:
    print("afternoon")
elif time >= 18 and time <= 22:
    print("evening")        
else:
    print("out of hours")    
