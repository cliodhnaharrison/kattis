n, k = map(int, input().split())
ratings = []

for _ in range(k):
    ratings.append(int(input()))

max_rating = (((n - k) * 3) + sum(ratings)) / n
min_rating = (((n - k) * -3) + sum(ratings)) / n

print(min_rating, max_rating)
