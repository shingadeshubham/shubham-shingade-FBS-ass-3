f = int(input("Enter feet: "))
i = int(input("Enter inches: "))
cm = f*30.48 + i*2.54
m = cm/100
print("Meters =", m)
print("Centimeters =", cm)
