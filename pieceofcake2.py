n, h, v = map(int, input().split())

slice_one = h * v * 4
slice_two = h * (n - v) * 4
slice_three = (n - h) * v * 4
slice_four = (n - h) * (n - v) * 4

print (max(slice_one, slice_two, slice_three, slice_four))
