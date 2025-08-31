height = int(input("Enter height of the wall: "))
width = int(input("Enter width of the wall: "))
cost_per_sqm = int(input("Enter cost of painting : "))

if height > 0 and width > 0 and cost_per_sqm > 0:
    area = height * width
    total_area = 4 * area
    total_cost = total_area * cost_per_sqm
    print("Total cost of painting:", total_cost)
else:
    print("Invalid input")
