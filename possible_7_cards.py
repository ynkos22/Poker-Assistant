import pandas as pd
import itertools
from Cards_class import Standard_deck
from Cards_class import Card




#Function that takes in:
#1. visible cards (as a list)
#2. additional cards (as a list) - this is optional and is used when you want to exclude certain cards from the deck (e.g. your own hand)

def seven_card_combinations(visible_cards, additional_cards=None):
    
    #removes visible cards from deck
    #.copy() is used to avoid changing the original Standard_deck
    remaining_deck = Standard_deck.copy()

    #removing the extra cards we want to exclude (point 2 above)
    if additional_cards is not None:
        for card in additional_cards:
            remaining_deck.remove(card)

    #removing the visible cards on the table from the "ingridients" used to make the 7 card combinations
    for card in visible_cards:
        remaining_deck.remove(card)

    
    #Finds how many additional cards we need for a total of 7 cards
    how_many_needed = 7 - len(visible_cards)
    

    #itertools.combinations(remaining_deck, how_many_needed) is an object that can be turned into a list
    #each combination is a tuple inside the "list"
    possible_new_card_combinations = itertools.combinations(remaining_deck, how_many_needed)
    possible_seven_card_combinations = []


    for combination in possible_new_card_combinations:
        
        seven_card = []

        #adds each card from a combination (tuple) to seven_card
        for i in range(0, how_many_needed):
            seven_card.append(combination[i])

        #adds visible cards to the seven card hand
        for card in visible_cards:
            seven_card.append(card)

        #saves our seven-card hand combination
        possible_seven_card_combinations.append(seven_card)

    return possible_seven_card_combinations

    



