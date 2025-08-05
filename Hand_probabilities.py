import math
import numpy as np
import random
from Cards_class import Standard_deck
from Cards_class import Card
from Cards_class import Hand
import itertools
import pandas as pd





#prints dataframe probabilities for round k
def probability(visible_cards, k):
    def combinations_of_k_cards(deck, k):
        return list(itertools.combinations(deck, k))

    remaining_deck = [card for card in Standard_deck if card not in visible_cards]

    data = {"Hands": [Hand(visible_cards + list(combinations_of_k_cards(remaining_deck, k)[i])) for i in range(len(combinations_of_k_cards(remaining_deck, k)))]}
    df = pd.DataFrame(data)

    #Adds new columns 
    df["Pair"] = df["Hands"].apply(lambda x: x.pair())
    df["2 Pairs"] = df["Hands"].apply(lambda x: x.double_pair())
    df["3 of a kind"] = df["Hands"].apply(lambda x: x.triple())
    df["Straight"] = df["Hands"].apply(lambda x: x.straight())
    df["Flush"] = df["Hands"].apply(lambda x: x.flush())
    df["Full House"] = df["Hands"].apply(lambda x: x.full_house())
    df["4 of a kind"] = df["Hands"].apply(lambda x: x.quadruple())
    df["Straight Flush"] = df["Hands"].apply(lambda x: x.straight_flush())
    df["Royal Flush"] = df["Hands"].apply(lambda x: x.royal_flush())

    #new dataframe with probabilities
    new_data = {"Types": ["Pair", "2 Pairs", "3 of a kind", "Straight", "Flush", "Full House", "4 of a kind", "Straight Flush", "Royal Flush"],
                "Probability": [df["Pair"].mean(), df["2 Pairs"].mean(), df["3 of a kind"].mean(), df["Straight"].mean(), df["Flush"].mean(), df["Full House"].mean(), df["4 of a kind"].mean(), df["Straight Flush"].mean(), df["Royal Flush"].mean()]}
    new_df = pd.DataFrame(new_data)
    return new_df










