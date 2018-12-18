hand = map(str, input().split())

card_type = [h[0] for h in hand]
strengths = [card_type.count(x) for x in card_type]

print (max(strengths))
