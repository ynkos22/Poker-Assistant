
from Cards_class import Standard_deck
from Cards_class import Card
from Cards_class import Hand







def inputs(input_string):
    list = input_string.split(", ")
    initial_hand = []
    for card in list:
        initial_hand.append([card[0], int(card[1])])

    new_hand = []
    for card in initial_hand:
        new_hand.append(Card(card[1], card[0]))

    return new_hand







