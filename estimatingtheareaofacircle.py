from math import pi

r, m, c = map(float, input().split())

while r != 0 and m != 0 and c != 0:
	area = pi * r * r
	estimated_area = (c * 2 * r * 2 * r) / m
	print (area, estimated_area)

	r, m, c = map(float, input().split())
