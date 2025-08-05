import pandas as pd
import numpy as np
import math
import random
from Cards_class import Card
from Cards_class import Hand
from Hand_probabilities import probability
from Input_translator import inputs



first_5_cards = input("Enter the first 5 cards (SuitValue notation): ")
translated_hand = inputs(first_5_cards)
print("Translated Hand:", translated_hand)
probabilities_round_1 = probability(translated_hand, 2)
print("Probabilities for round 1:")
print(probabilities_round_1)
first_6_cards = input("Enter the first 6 cards (SuitValue notation): ")
translated_hand_2 = inputs(first_6_cards)
probabilities_round_2 = probability(translated_hand, 1)
print("Probabilities for round 2:")
print(probabilities_round_2)