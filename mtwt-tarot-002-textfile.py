# Open the file 'tarot-cards.txt' in read mode using a with statement
with open('tarot-cards.txt') as var:
    # Read all lines from the file and store them in a list called 'lines'
    lines = var.readlines()

    # Create a dictionary called 'cards' by splitting each line at the first ': ' encountered
    # The left part becomes the key (card), and the right part becomes the value (meaning)
    cards = dict(line.strip().split(': ', 1) for line in lines)


for card, meaning in cards.items():
    print(f"{card}: {meaning}")

