radius, crust = map(int, input().split())

area = radius ** 2

cheese_area = (radius - crust) ** 2

percentage_cheese = (cheese_area / area) * 100

print (percentage_cheese)
