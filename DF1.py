import pandas as pd
import numpy as np
from Cards_class import Card
from Cards_class import Hand
from Cards_class import Standard_deck
import itertools
from possible_7_cards import seven_card_combinations
from largest_5_card import biggest_5_hand


#function that scores a 5 card hand. Higher score means better hand
#takes in a 5-card hand (a poker hand)
def score(hand_list):
    our_hand = Hand(hand_list)
    if our_hand.royal_flush() == True:
        #this will guarantee highest score
        return 100000000000
    elif our_hand.straight_flush() == True:
        #what value of the card the straight ends with dictates its score
        #the division by 10 ensures it won't surpass royal flush
        return (our_hand.hand[-1].value/10)*10000000000 
    elif our_hand.quadruple() == True:
        return our_hand.hand[-1].value/10*1000000000
    elif our_hand.full_house() == True:
        #the first term is about the triple, and second term the pair
        #the 5-card hand always lists the triple first, then the pair
        return ((our_hand.hand[0].value/10)*100000000+(our_hand.hand[-1].value))
    elif our_hand.flush() == True:
        return (our_hand.hand[-1].value/10)*10000000
    elif our_hand.straight() == True:
        return (our_hand.hand[-1].value/10)*1000000
    elif our_hand.triple() == True:
        return (our_hand.hand[-1].value/10)*100000
    elif our_hand.double_pair() == True:
        #the first term is about the highest pair, and second term the second pair
        return ((our_hand.hand[0].value/10)*10000+(our_hand.hand[-1].value))
    elif our_hand.pair() == True:
       return (our_hand.hand[-1].value/10)*10000
    else:
        return our_hand.hand[-1].value


#function that creates sorted dataframe from a set of visible cards (and additional cards(optional) to be removed from the deck)
def dataframe1(visible_cards, additional_cards=None):
    data = {
        "7 card combinations": seven_card_combinations(visible_cards, additional_cards=additional_cards)
    }

    DF1 = pd.DataFrame(data)

    #adds a column with the best 5 card hand from each 7 card combination
    DF1["Best 5 card hand"] = DF1["7 card combinations"].apply(biggest_5_hand)
    #adds a column with the score of each best 5 card hand
    DF1["Hand rank"] = DF1["Best 5 card hand"].apply(score)
    return DF1

#takes in a dataframe and sorts it by hand rank
#returns the sorted dataframe
def sort_dataframe(DF):
    DF = DF.sort_values(by=["Hand rank"], ascending=False).reset_index(drop=True)
    return DF