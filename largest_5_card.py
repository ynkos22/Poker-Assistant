
from Cards_class import Card
from Cards_class import Hand
from Cards_class import Standard_deck

#Finds the largest 5-card poker hand within a 7-card hand




#function that returns all the cards of the suit with the most cards (the cards closest to a flush)
#takes in list of Card objects and outputs a list of Card objects
def suit_filter(my_hand):
    #make it an object
    our_hand = Hand(my_hand) 

    suits = our_hand.which_suit_and_how_many()

    #finds the suit with highest frequency. This is a list with first element being the suit and second its frequency e.g ["H", 3]
    flush_suit_frequency = max(suits, key=lambda suit_frequency: suit_frequency[1])

    #first element of flush_suit_frequency is the suit:
    flush_suit = flush_suit_frequency[0]

    #filter so that all the cards are of the suit you have the most of. 
    only_of_this_suit = [card for card in our_hand.hand if card.suit == flush_suit]

    return only_of_this_suit


#function that returns all the cards of the same value as the value with the most cards (the cards closest to a triple or quad)
#takes in list of Card objects and outputs a list of Card objects
def value_filter(my_hand):
    #initializes the object from my_hand(a list of Card objects)
    
    our_hand = Hand(my_hand) 

    #reverses the list so that if there are multiple values with the same frequency, it takes the highest value
    value_frequencies = our_hand.which_value_and_how_many()[::-1]

    #finds the value with highest frequency. This is a list with first element being the value and second its frequency e.g [2, 3] meaning 3 two's
    max_frequency_value_its_frequency = max(value_frequencies, key=lambda value_frequency: value_frequency[1])

    #first element of max_frequency_value_its_frequency is the value:
    max_frequency_value = max_frequency_value_its_frequency[0]

    #filter so that all the cards are of the suit you have the most of. 
    only_of_this_value = [card for card in our_hand.hand if card.value == max_frequency_value]

    return only_of_this_value



#function that removes card with duplicate values from a list of cards
#takes in list of card objects, and outputs a list of card objects.
def remove_duplicates(input_list):
    #adds the first card to the new list
    new_list = [input_list[0]]

    #loops through the rest of the cards
    for card in input_list[1:]:
        duplicate_found = False

        #for each card in input list it checks if there is a card with the same value in the new list
        #if there is, it does not add it to the new list
        #if there is not, it adds it to the new list
        for card2 in new_list:
            if card.value == card2.value:
                duplicate_found = True
                break   # stop checking — we know it's a duplicate
        if not duplicate_found:
            new_list.append(card)
    return new_list


#function that finds the biggest 5 card hand within a 7 card hand
#takes in list of card objects, and outputs a list of card objects
def biggest_5_hand(input_hand):
    our_hand = Hand(input_hand)

    if our_hand.royal_flush() == True:
        suited_hand_list = suit_filter(our_hand.hand) #returns cards of only one suit as a list.

        #remove duplicate value cards
        unfiltered_list = suited_hand_list
        filtered_list = remove_duplicates(unfiltered_list)
        
        filtered_hand = Hand(filtered_list)
        #loop through last 5 cards and see if they are consecutive
        filtered_sorted_hand = filtered_hand.hand #this is a list
        
        return filtered_sorted_hand[-5:] #since the hand is sorted from small to big, the last 5 elements will have the 5 biggest values.
    
    elif our_hand.straight_flush() == True:
        suited_hand_list = suit_filter(our_hand.hand) #returns cards of only one suit as a list.

        #remove duplicate value cards
        unfiltered_list = suited_hand_list
        filtered_list = remove_duplicates(unfiltered_list)

        #initializes the hand object to sort it
        filtered_hand = Hand(filtered_list)

        #loop through last 5 cards and see if they are consecutive
        filtered_sorted_hand = filtered_hand.hand #this is a list
        reversed_hand = filtered_sorted_hand[::-1] #instead of small to big it is now big to small, easier to loop from index 0.
        
        #here we need to WHERE the straight is
        #not necessarily the last 5 cards
        #checks for consecutive values
        for i in range(0, len(reversed_hand)-4):
            if reversed_hand[i+1].value == reversed_hand[i].value-1 and reversed_hand[i+2].value == reversed_hand[i+1].value - 1 and reversed_hand[i+3].value == reversed_hand[i+2].value - 1 and reversed_hand[i+4].value == reversed_hand[i+3].value - 1:
                return [reversed_hand[i+4], reversed_hand[i+3], reversed_hand[i+2], reversed_hand[i+1], reversed_hand[i]] #returns in ascending order
            else:
                continue
            
    elif our_hand.quadruple() == True:
        #if there is a quad, then it must be the value with the highest frequency
        quad = value_filter(our_hand.hand) #returns cards of only one value as a list.
        return quad

    elif our_hand.full_house() == True:
        hand = our_hand.hand
        triple = value_filter(our_hand.hand) #returns cards of only one value as a list.

        #removes the cards in the triple from the hand so that they are not found again when searching for a pair
        for card in triple:
            hand.remove(card)
        
        pair = [value_filter(hand)[0], value_filter(hand)[1]] #we do this in case there are 2 triples.

        #adds the pair to the triple to make a full house
        #"triple" is now a full house
        for card in pair:
            triple.append(card)

        return triple
    
    
    elif our_hand.flush() == True:
        suited_hand_list = suit_filter(our_hand.hand) #returns cards of only one suit as a list. The suit with the most cards.
        suited_hand_object = Hand(suited_hand_list) #makes that list an object (to sort it)

        flush = suited_hand_object.hand[-5:] #since the hand is sorted from small to big, the last 5 elements will have the 5 biggest values. 
        return flush
    

    elif our_hand.straight() == True:
        #remove duplicate value cards
        unfiltered_list = our_hand.hand
        filtered_list = remove_duplicates(unfiltered_list)
        
        #initializes the hand object to sort it
        filtered_hand = Hand(filtered_list)

        
        filtered_sorted_hand = filtered_hand.hand #this is a list
        reversed_hand = filtered_sorted_hand[::-1] #instead of small to big it is now big to small  
        
        #here we need to WHERE the straight is
        #not necessarily the last 5 cards
        #checks for consecutive values
        for i in range(0, len(reversed_hand)-4):
            if reversed_hand[i+1].value == reversed_hand[i].value-1 and reversed_hand[i+2].value == reversed_hand[i+1].value - 1 and reversed_hand[i+3].value == reversed_hand[i+2].value - 1 and reversed_hand[i+4].value == reversed_hand[i+3].value - 1:
                return [reversed_hand[i], reversed_hand[i+1], reversed_hand[i+2], reversed_hand[i+3], reversed_hand[i+4]]
            else:
                continue


    elif our_hand.triple() == True:
        #we can do this because if there is a triple, it must be the value with the highest frequency
        #no quads if it reached here
        #cannot have 2 triples, since that would be a full house
        triple = value_filter(our_hand.hand) #returns cards of only one value as a list.
        return triple
    
    elif our_hand.double_pair() == True:
        #finds the first pair
        hand = our_hand.hand
        pair1 = value_filter(hand)

        #removes the cards in the first pair from the hand so that they are not found again when searching for a second pair
        for card in pair1:
            hand.remove(card)
        
        #finds the second pair
        pair2 = value_filter(hand)

        #adds the second pair to the first pair to make a double pair
        for card in pair2:
            pair1.append(card)

        #"pair1" is now a double pair
        return pair1
    

    elif our_hand.pair() == True:
        pair = value_filter(our_hand.hand) #returns cards of only one value as a list.
        return pair
    

    else:
        #if there is no pair, then the best hand is just the highest card
        #the highest card is the last card in the sorted hand
        return [our_hand.hand[-1]]


