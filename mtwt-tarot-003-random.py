import random

with open('tarot-cards.txt') as var:
    lines = var.readlines()
    cards = dict(line.strip().split(': ', 1) for line in lines)

# Shuffle the cards and draw three random cards
card_names = list(cards.keys())
random.shuffle(card_names)
reading = card_names[:3]

# Print the drawn cards with significance
print("Your tarot card reading is:")
for card in reading:
    print(f"{card}: {cards[card]}")
