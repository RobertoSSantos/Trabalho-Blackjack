import random

from q_table_player_1 import *

agent = RLAgent()

import sys

# This player choose your decision based only on your hand.

# Card values
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
               'jack': 10, 'queen': 10, 'king': 10, 'ace': [1, 11]}

# Function to calculate hand value
def calculate_hand_value(hand):
    value = 0
    ace_count = 0
    for card in hand:
        #print(card)
        if card.value == 'ace':
            ace_count += 1
        else:
            value += card_values[card.value]

    for _ in range(ace_count):
        if value + 11 <= 21:
            value += 11
        else:
            value += 1

    return value
    
class Player_1:
  def decision(self, your_hand, dealer_card, round_num, total_rounds):
    print("Player current hand", [d for d in your_hand])  
    print(f"Making decision...\n")       

    if round_num < total_rounds * (float(sys.argv[2])):
      choice = random.choice(["hit", "stop"])
    else:
      choice = agent.decision(calculate_hand_value(your_hand))

    print("You made the decision ", choice)
    print("------------------- ", choice)
    return choice

  def result(self, your_hand, dealer_hand, decision, reward, is_not_done):
    print("Your hand is ", your_hand)
    print("Reward :", reward, " is_not_done? ", is_not_done)  
    print("==================== ")    
    return reward
  