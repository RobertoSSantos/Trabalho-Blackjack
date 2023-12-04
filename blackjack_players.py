import sys, random
from q_table_player import *

# Card values
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
               'jack': 10, 'queen': 10, 'king': 10, 'ace': [1, 11]}

def basic_strategy_master(player_hand, dealer_card):
  print("Using basic strategy!")
  
  dealer_last_card = calculate_hand_value(dealer_card[:1])

  if(calculate_hand_value(player_hand) >= 17): 
    return 'stop'
  elif ('ace' and '7' in player_hand) and (('jack' or '10' or 'queen' or 'king' or 'ace') == dealer_last_card):
    return 'hit'
  elif ('12' in player_hand) and (('4' or '5' or '6') == dealer_last_card):
    return "stop"
  elif 13 <= calculate_hand_value(player_hand) <= 16 and 2 <= dealer_last_card <= 6:
    return "stop"
  else:
    return agent.decision(calculate_hand_value(player_hand))

agent = RLAgent()

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

###################################### PLAYER SIMPLE START ######################################
class Player_simple: # This player choose your decision based only on your hand.
  def decision(self, player_hand, dealer_card, round_num, total_rounds):
    print("Player current hand", [d for d in player_hand])  
    print(f"Making decision...\n")       

    if round_num < total_rounds * (float(sys.argv[2])):
      choice = random.choice(["hit", "stop"])
    else:
      choice = agent.decision(calculate_hand_value(player_hand))

    print("You made the decision: ", choice)

    return choice

  def result(self, player_value, dealer_value, is_not_done):
    print("Your hand is ", player_value)
    reward = 0

    if (player_value > 21):
      reward = -1
    elif (dealer_value > 21):
      reward = +1
    elif (player_value >= dealer_value):
      reward = +1
    elif (player_value == dealer_value):
      reward = 0
    else:
      reward = -1

    print(f"Reward : {reward} finished? {is_not_done} \n ====================")     
    return reward
###################################### PLAYER SIMPLE END ######################################

###################################### PLAYER DOUBLE START ######################################
class Player_double: # This player choose your decision based only on your hand and dealer's card
  def decision(self, player_hand, dealer_card, round_num, total_rounds):
    print("Player current hand", [d for d in player_hand])  
    print(f"Making decision...\n")       

    if round_num < total_rounds * (float(sys.argv[2])):
      choice = random.choice(["hit", "stop"])
    else:
      choice = agent.decision(tuple(( calculate_hand_value(player_hand), calculate_hand_value(dealer_card[:1]))))

    print("You made the decision ", choice)
    print("------------------- ", choice)
    return choice

  def result(self, player_value, dealer_value, is_not_done):
    print("Your hand is ", player_value)
    reward = 0

    if (player_value > 21):
      reward = -1
    elif (dealer_value > 21):
      reward = +1
    elif (player_value >= dealer_value):
      reward = +1
    elif (player_value == dealer_value):
      reward = 0
    else:
      reward = -1

    print(f"Reward : {reward} finished? {is_not_done} \n ====================")     
    return reward
###################################### PLAYER DOUBLE END ######################################

###################################### PLAYER MASTER START ######################################
class Player_master:
  def decision(self, player_hand, dealer_card, round_num, total_rounds):
    print("Player current hand", [d for d in player_hand])  
    print(f"Making decision...\n")       
    choice = basic_strategy_master(player_hand, dealer_card)
    print("You made the decision ", choice)
    print("------------------- ", choice)
    return choice

  def result(self, player_value, dealer_value, is_not_done):
    print("Your hand is ", player_value)
    reward = 0

    if (player_value > 21):
      reward = -1
    elif (dealer_value > 21):
      reward = +1
    elif (player_value >= dealer_value):
      reward = +1
    elif (player_value == dealer_value):
      reward = 0
    else:
      reward = -1

    print(f"Reward : {reward} finished? {is_not_done} \n ====================")     
    return reward
###################################### PLAYER MASTER END ######################################

