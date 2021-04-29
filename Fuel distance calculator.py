print ("___________Fuel Distance Program____________")

tankSize = (int(input("Size of Tank: ")))
percentFull = (int(input("Percent Full: ")))
L100Km = (int(input("L/100km: "))) #Round up to nearest number
distance = (int(input("Distance to Travel: ")))
distanceToEmpty = (((tankSize-5)*percentFull) / L100Km)
remainingFuel = ((distanceToEmpty - distance)/L100Km)

if ( distanceToEmpty >= distance):
    print("You can go another", (format(distanceToEmpty,".1f")), "Km")
    print("Your will make it to your destination with", (format(remainingFuel,".1f")), "L to spare")

else:
    print("You can go another", (format(distanceToEmpty,".1f")), "Km")
    print("Your won't be able to make it to your destination")
    print("Your will need an extra", (format(remainingFuel,".1f").replace("-","")), "L of fuel to make it to your destination") 
    print("Please stop at the next fuel station")
                
            
                
