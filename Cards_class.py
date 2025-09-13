import math
import numpy as np
import random


#Defining the objects we will need - Card, Hand

class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __repr__(self):
        return f"{self.suit}: {self.value}"
    def __eq__(self, other):
        return isinstance(other, Card) and self.value == other.value and self.suit == other.suit

    def __hash__(self):
        return hash((self.value, self.suit))
    
class Hand:

    def __init__(self, hand):
        self.hand = sorted(hand, key = lambda card: card.value)

    def __repr__(self):
        return str(self.hand)

    #Finds the longest chain (cards with consecutive numbers) in the hand and returns the length of it
    def longest_chain(self):
        
        #replaces each card in the hand with its value, and removes duplicates
        #distinct_values_only is a numpy array
        distinct_values_only = np.unique([card.value for card in self.hand])
        
        longest = 0
        current_length = 1
        
        #loops through hand checking if previous element is 1 less than the current if so increment "current_length"
        for i in range(1, len(distinct_values_only)):

            #increments "chain" length if it finds consecutive numbers
            #note: the elements in the list "distinct_values_only" are numbers NOT cards
            if distinct_values_only[i] == distinct_values_only[i - 1] + 1:
                current_length += 1
            else:
                #saves the longest chain
                longest = max(longest, current_length)
                current_length = 1
        
        longest = max(longest, current_length)
        return longest

    # Count how many cards have the same value and which value
    def which_value_and_how_many(self):
        
        #returns a tuple of elements
        #each element is an array with first element beging the distinct card value and second element being how many times it appears in the hand
        #e.g ([1, 2], [5, 3]) meaning two 1s and three 5s
        unique_card_values = np.unique([(card.value) for card in self.hand], return_counts=True)

        #making it a list is easier to work with
        #makes a new list with first element being a distinct card (the object), and the second element being how many times it appears in the hand. 
        which_value_how_many_times = [[unique_card_values[0][i], int(unique_card_values[1][i])] for i in range(len(unique_card_values[0]))]

        #returns something like [[1, 5], [2, 3]] meaning five 1s and three 2s
        return which_value_how_many_times

    # Counts how many cards of each suit
    def which_suit_and_how_many(self):
        
        #map each card to its suit and put them into a list
        #returns a tuple of the suits in the hand and how many of each: e.g (["D", "S"], [3, 5])
        unique_card_suits = np.unique([card.suit for card in self.hand], return_counts=True)

        #pairs each card suit with how many times it appears. e.g [["D", 3], ["S", 5]]
        which_suit_how_many_times = [[unique_card_suits[0][i], int(unique_card_suits[1][i])] for i in range(len(unique_card_suits[0]))]

        #returns something like [["D", 3], ["S", 5]], where the first item in each sublist is the suit and second item is its frequency
        return which_suit_how_many_times
    #returns how many pairs in hand
    def how_many_pairs(self):
        #this counts how many pairs there are in the hand
        counter = 0

        #each card_frequency is a list of 2 numbers e.g [1, 2], meaning 2 1s, i.e first value is the value of the card and second is the frequency of that card within the hand
        for card_frequency in self.which_value_and_how_many():
            
            #we only care about the frequency so we iterate through only the second element card_frequency[1]
            #if it is 2 or larger it counts as a pair
            if card_frequency[1] >= 2:
                counter += 1

        return counter
    
    #returns True if there exists a triple and False if not
    def triple(self):
        #default set to False
        triple = False

        #loops through all the distinct card values and their frequency 
        for card_frequency in self.which_value_and_how_many():
            
            #if any frequency is 3 or larger that means there is a triple and the function will return True
            #card_frequency is a list of 2 numbers e.g [1, 3] meaning 3 1s
            if card_frequency[1] >= 3:
                triple = True
                break
            else:
                None
        return triple
    
    #returns True if there is a quadruple (4 of a kind), otherwise False 
    #same process as triple function - therefore not commented in detail
    def quadruple(self):
        quadruple = False
        for card_frequency in self.which_value_and_how_many():

            if card_frequency[1] == 4:
                quadruple = True
                break
            else:
                None
        return quadruple
    
    #returns True if there is a pair, otherwise False
    def pair(self):
        #default set to False
        pair = False

        #loops through all the distinct card values and their frequency 
        for card_frequency in self.which_value_and_how_many():
            
            #if any frequency is 2 or larger that means there is a pair and the function will return True
            if card_frequency[1] >= 2:
                pair = True
                break
            else:
                None
        return pair
    #returns True if there are 2 or more pairs
    def double_pair(self):
        #how_many_pairs() counts how many pairs in hand and if this is greater or equal to 2 it will return True, otherwise False
        if self.how_many_pairs() >= 2:
            return True
        else:
            return False
    
    #returns True if there is a straight in hand, otherwise False. 
    def straight(self):
        #longest chain return the length of the longest chain in a hand. 
        #If this is 5 or longer it counts as a straight and it returns True, otherwise False
        if self.longest_chain() >= 5:
            return True
        else:
            return False
    
    #returns True if there is a flush in hand, otherwise False.
    def flush(self):
        #makes a list of the frequency of each suit
        suit_frequencies = self.which_suit_and_how_many()

        #finds the suit with the highest frequency - this is the suit with the flush
        #max function returns the list with the highest second element (the frequency), e.g ["H", 4], but we only want the suit so we take the first element of this list hence [0].
        flush_suit = max(suit_frequencies, key=lambda x: x[1])[0]
    
        #filters our hand so that only cards with this suit remains
        only_of_this_suit = [card for card in self.hand if card.suit == flush_suit]

        #more than 5 cards of this suit means there is a flush
        if len(only_of_this_suit) >= 5:
            return True
        else:
            return False
                
    # Check for a royal flush in the hand, returns True if there is a royal flush and False if not
    def straight_flush(self):
        #Checks for straight, and flush
        #filters so that only cards of the suit with the flush remains
        #then checks if there is a straight in this filtered hand


        #checks if there is a straight AND a flush to reduce computation
        if self.flush() == False or self.straight() == False:
            return False
        
        #if this is true it enters here
        else:
            
            #makes a list of the frequency of each suit
            suit_frequencies = self.which_suit_and_how_many()

            #finds the suit with the highest frequency - this is the suit with the flush
            flush_suit = max(suit_frequencies, key=lambda x: x[1])[0]
        
            #filters our hand so that only cards with this suit remains
            only_of_this_suit = [card for card in self.hand if card.suit == flush_suit]

            #makes a temporary hand with only the cards of this suit
            temporary_hand = Hand(only_of_this_suit)

            #checks if there is a straight in this hand
            if temporary_hand.straight() == True:
                return True
            else:
                return False
    #returns True if there is at least 1 full house in the hand, otherwise False
    def full_house(self):
        #this is a list
        values_frequencies = self.which_value_and_how_many()

        # First, look for any triple (or better)
        triple_value = None
        
        #looks for values with frequency 3 or more, then adds this value to triple_value
        for value_frequency in values_frequencies:
            if value_frequency[1] >= 3:
                triple_value = value_frequency[0]
                break

        if triple_value is None:
            return False  # no triple at all so cannot be full house

        # Now look for a pair among the *other* values
        for value_frequency in values_frequencies:
            if value_frequency[0] == triple_value:
                continue  # skip the triple’s value
            if value_frequency[1] >= 2:
                return True  # found a valid pair

        return False
    
   
        
    #returns True if there is a straight flush, otherwise False
    def royal_flush(self):
        #default set to False

        royal_flush = False

        #first check if there is a straight flush
        if self.straight_flush() == False:
            return False
        else:

            suit_frequencies = self.which_suit_and_how_many()

            #finds the suit with the highest frequency - this is the suit with the flush
            flush_suit = max(suit_frequencies, key=lambda x: x[1])[0]
        
            #filters our hand so that only cards with this suit remains
            only_of_this_suit = [card for card in self.hand if card.suit == flush_suit]

            #makes a temporary hand with only the cards of this suit
            temporary_hand = Hand(only_of_this_suit)

            #removes repeats
            only_unique_values = np.unique([card.value for card in temporary_hand.hand])

            #slices the previous list so that it only has the 5 largest cards
            #it is already sorted so we can just take the last 5 elements
            highest_five_cards = only_unique_values[-5:]

            #there is only 1 way to get royal flush
            if list(highest_five_cards) == [10, 11, 12, 13, 14]:
                return True
            else:
                return False


# Standard deck of cards
Standard_deck = [Card(2, "H"), Card(3, "H"), Card(4, "H"), Card(5, "H"), Card(6, "H"), Card(7, "H"), Card(8, "H"), Card(9, "H"), Card(10, "H"), Card(11, "H"), Card(12, "H"), Card(13, "H"), Card(14, "H"),
           Card(2, "D"), Card(3, "D"), Card(4, "D"), Card(5, "D"), Card(6, "D"), Card(7, "D"), Card(8, "D"), Card(9, "D"), Card(10, "D"), Card(11, "D"), Card(12, "D"), Card(13, "D"), Card(14, "D"),
           Card(2, "S"), Card(3, "S"), Card(4, "S"), Card(5, "S"), Card(6, "S"), Card(7, "S"), Card(8, "S"), Card(9, "S"), Card(10, "S"), Card(11, "S"), Card(12, "S"), Card(13, "S"), Card(14, "S"),
           Card(2, "C"), Card(3, "C"), Card(4, "C"), Card(5, "C"), Card(6, "C"), Card(7, "C"), Card(8, "C"), Card(9, "C"), Card(10, "C"), Card(11, "C"), Card(12, "C"), Card(13, "C"), Card(14, "C")]
        






