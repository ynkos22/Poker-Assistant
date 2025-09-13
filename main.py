import pandas as pd
import numpy as np
from Cards_class import Card
from Cards_class import Hand
from Cards_class import Standard_deck
import itertools
from possible_7_cards import seven_card_combinations
from largest_5_card import biggest_5_hand
from DF1 import dataframe1
from DF1 import score
from DF1 import sort_dataframe




#cards_on_table = [Card(10, "H"), Card(11, "H"), Card(12, "H"), Card(13, "H")]

#cards_in_hand = [Card(3, "S"), Card(3, "H")]

#function that calculates the probability of winning given the cards on the table and the cards in your hand
def winning_probability(cards_on_table, cards_in_hand):
    
    your_cards = cards_in_hand + cards_on_table

    #dataframe with all possible 7-card combinations from your cards and their best 5-card hands and scores
    your_odds = dataframe1(your_cards)

    #dataframe with all possible 7-card combinations from the table cards and their best 5-card hands and scores where your hand is removed from the deck
    their_odds = dataframe1(cards_on_table, additional_cards=cards_in_hand)


    indices = []
 

    #takes each row in your_odds,
    #adds the row to their_odds,
    #sorts their_odds in terms of hand rank,
    #finds the index of your hand in sorted_odds,
    #the index is proportional to the probability of winning with that hand,
    #saves the index to "indices"
    #removes your hand from sorted_odds so that the next iteration works correctly
    for row in your_odds.itertuples(): #first element in row is the index, so row[1] is the 7-card combination, row[2] the best 5-card hand, row[3] the hand rank

        their_odds.loc[len(their_odds)] = list(row)[1:5] #adds the row to their_odds, excluding the index

        #sorts their_odds in terms of hand rank
        sorted_odds = sort_dataframe(their_odds)

        #finds the index of your hand in sorted_odds
        for row2 in sorted_odds.itertuples():
            if row2[2] == row[2]:
                row_index = row2[0]
                #removes your hand from sorted_odds so that the next iteration works correctly
                sorted_odds.drop(index=row_index, inplace=True)
                #saves the index to "indices"
                indices.append(row_index)
                break
    
    winning_probabilities = []

    #calculates the winning probability for each of your hands and saves it to winning_probabilities
    length_of_their_hand = len(sorted_odds) #how many different 7-card combinations the opponent can have

    length_of_your_hand = len(your_odds) #how many different 7-card combinations you can have

    for i in indices:
        percentage_it_does_not_beat = i/length_of_their_hand
        #the probability of winning is 1 minus the probability of not winning
        probability = 1-percentage_it_does_not_beat
        winning_probabilities.append(probability)


    #each hand is equally likely, let's say with probability p, so the total probability of winning is p * sum of condidtional probabilities
    #p = 1/length_of_your_hand
    #conditional_probability = each element in winning_probabilities is the conditional probability of winning given that hand
    unconditional_probability = sum(winning_probabilities)/length_of_your_hand

    return unconditional_probability


#function that translates input string into list of Card objects
def translator(input_string):
    list = input_string.split(", ")
    initial_hand = []


    #for each element in list: eg "3D"
    #we append [value, suit] to initial_hand e.g [3, "D"]
    for card in list:
        if len(card) == 3:
            #"13D" becomes [13, D]
            card_value = int(card[0:2])
            card_suit = card[2]
            initial_hand.append([card_value, card_suit])
        else:
            card_value = int(card[0])
            card_suit = card[1]
            initial_hand.append([card_value, card_suit])


    new_hand = []

    #makes each [value, suit] pair in initial_hand into Card objects
    for card in initial_hand:
        card_value = card[0]
        card_suit = card[1]
        new_hand.append(Card(card_value, card_suit))

    return new_hand





#Here we will run everything together


def game():
    cards_on_table_input = input("What cards are on the table? (ValueSuit)")
    cards_in_hand_input = input("What cards do you have? (ValueSuit)")

    cards_on_table = translator(cards_on_table_input)
    cards_in_hand = translator(cards_in_hand_input)

    current_winning_probability = winning_probability(cards_on_table, cards_in_hand)
    
    print(f"Your current probability of winning is {current_winning_probability*100:.2f}%")

    fourth_card = input("What is the fourth card on the table? (ValueSuit)")
    cards_on_table.append(translator(fourth_card)[0])

    new_winning_probability = winning_probability(cards_on_table, cards_in_hand)
    print(f"Your new probability of winning is {new_winning_probability*100:.2f}%")

game()
