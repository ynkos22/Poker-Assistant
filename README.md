# Poker-Assistant
Probability and EV algorithm for best poker performance.

Brief description of each file:

Cards_class.py: Setting up objects classes for cards and hands that will be used throughout

Hand_probabilities.py: Calculating the probability of obtaining certain hands given the visible cards

Expected_values.py: Uses probabilities to calculate expected values of different bet sizes

Betting_strategy.py: Takes into account expected values, but prevents all-in situations and implements times to fold.

main.py: Where everything will run.
