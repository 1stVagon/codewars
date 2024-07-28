def draw(deck):
    drawn_deck = []
    temp_deck = []

    while len(deck) != 0:
        drawn_deck.append(deck[0])
        deck.pop(0)

        if len(deck) != 0:
            temp_deck.append(deck[0])
            deck.pop(0)
            deck.append(temp_deck[0])
            temp_deck.clear()

    return drawn_deck
