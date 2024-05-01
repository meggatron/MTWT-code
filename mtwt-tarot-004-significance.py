import random

with open('tarot-cards.txt') as var:
    lines = var.readlines()
    cards = dict(line.strip().split(': ', 1) for line in lines)

card_names = list(cards.keys())
random.shuffle(card_names)
reading = card_names[:3]

# Assign significance to each card
significances = ["Signifying Your Past", "Signifying Your Present", "Signifying Your Future"]
reading_with_significance = list(zip(significances, reading))

# Print the drawn cards with significance
print("Your tarot card reading is:")
for significance, card in reading_with_significance:
    print(f"{significance}: {card}: {cards[card]}")
