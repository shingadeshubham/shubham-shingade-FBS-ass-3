area = float(input("Enter area of one wall: "))
int_cost = float(input("Enter interior cost per unit: "))
ext_cost = float(input("Enter exterior cost per unit: "))


total = (4*area*int_cost) + (4*area*ext_cost)

print("Total Painting Cost =", total)
