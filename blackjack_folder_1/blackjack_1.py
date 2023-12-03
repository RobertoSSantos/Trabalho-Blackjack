import pygame
import random
import itertools
import sys

from player_1 import *
from q_table_player_1 import *

# Initialize Pygame
pygame.init()

# Game window settings
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Simple Blackjack')

portraits = [
  pygame.image.load(f'../portrait/jacare.png')
]

dealer_portrait_img = pygame.image.load(f'../portrait/dealer.png'),  

winner_image = pygame.transform.scale(pygame.image.load(f'../symbols/winner.png'), (200, 200))

# Load card images (assuming we have basic card images named as '2_of_clubs.png', '3_of_hearts.png', etc.)
card_images = {}
suits = ['hearts', 'diamonds', 'clubs', 'spades']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
player_portrait = pygame.transform.scale(random.choice(portraits), (80, 160))
dealer_portrait = pygame.transform.scale(random.choice(dealer_portrait_img), (80, 160))

for suit in suits:
    for value in values:
        image_scale = 0.5
        card_img =  pygame.image.load(f'../cards/{value}_of_{suit}.png')
        scaled_card = pygame.transform.scale(card_img, (int(200 * image_scale), int(300 * image_scale)))        
        card_images[(suit, value)] = scaled_card



# Draw card function
def draw_card(deck, hand):
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)
    return card

def render_card(card, pos):
    screen.blit(card_images[(card.suit, card.value)], pos) 
    
def render_hand(hand, pos):
    for idx, c in enumerate(hand):
      screen.blit(card_images[(c.suit, c.value)], pos)
      pos = (pos[0] + 120, pos[1])

def render_portrait(portrait, pos):
    screen.blit(portrait, pos) 

def render_winner(pos):
    screen.blit(winner_image, pos) 

class Card:
  def __init__(self, suit, value):
    self.value = value
    self.suit = suit
    
  def __repr__(self):
    return f'[{self.value}-{self.suit}]'
    
 ######################################
 #
 # Seu agente deve ser colocado nessa região
 # Lembre-se que a regra do blackjack foi modificada
 # nesse versão o dealer joga primeiro que você
 # e você joga vendo a primeira carta dele
 #
 #


class DealerPlayer:
  def decision(self, your_hand, dealer_hand):
    dealer_value = calculate_hand_value(dealer_hand)
    if dealer_value < 17:
      return "hit"
    else:
      return "stop"

  def result(self, your_hand, dealer_hand, decision, reward, is_not_done):
    print("Reward :", reward)
    pass

# Main game loop
def play_blackjack(player, round_num):
    running = True
    player_turn = False  # True if it's player's turn, False for dealer's turn
    dealer_turn = True
    
    # Create a deck of cards and deal initial hands
    # [rest of the initial setup is the same]
    deck = [Card(s,v) for s,v in itertools.product(suits, values)]
    player_hand = []
    dealer_hand = []
    hand_result = 0
    random.shuffle(deck)
    #print([d for d in deck])
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle player input here (e.g., hit or stand)
            # You can use keys or mouse clicks for player decisions

        screen.fill((0, 0, 0))  # Clear screen (black background)
        #render_card(deck[0], (100, 100))
        
        # Display the cards and scores

        if dealer_turn:
            # Dealer's turn logic
            dealer_value = calculate_hand_value(dealer_hand)
            if dealer_value < 17:
                draw_card(deck, dealer_hand) 
            else:
              dealer_turn = False
              player_turn = True       
        elif player_turn:
            # Player's turn logic
            # Implement hit or stand decision
            decision = player.decision(player_hand, dealer_hand[0], round_num, total_rounds)
            if decision == "hit":
              draw_card(deck, player_hand)
            else:
              player_turn = False

            if calculate_hand_value(player_hand) >= 21:
              player_turn = False                
               
            score = 0     
            
            if not player_turn:
              # Compare hands and decide winner
              player_value = calculate_hand_value(player_hand)
              if (player_value > 21):
                hand_result = -1
              elif (dealer_value > 21):
                hand_result = +1
              elif (player_value >= dealer_value):
                hand_result = +1
              elif (player_value == dealer_value):
                hand_result = 0
              else:
                hand_result = -1
              print(f"Round result {hand_result}")                     
              running = False
            
            # Result
            reward = player.result(player_hand, dealer_hand[0], decision, hand_result, player_turn)

            print(f"TIA DE GIULIA {player_hand}")
            if not running:
              if decision == "hit":
                agent.update_qtable(calculate_hand_value(player_hand[:-1]), decision, reward, player_value)
              else:
                agent.update_qtable(player_value, decision, reward, player_value)

        render_hand(player_hand, (150, 100))
        render_hand(dealer_hand, (150, 300))     
        render_portrait(player_portrait, (50, 100))
        render_portrait(dealer_portrait, (50, 300))                
        pygame.display.flip()  # Update the display
        #pygame.time.wait(100)  
        
    #pygame.time.wait(100)  

    return hand_result

# Insire seu jogador abaixo:
player = Player_1()

results = []
total_rounds = int(sys.argv[1])
train_percentage = float(sys.argv[2])

wins_num = 0
lose_num = 0

for i in range(total_rounds):
  print(f"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= Starting game: {i} =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
  results.append(play_blackjack(player, i))

end = int(total_rounds * (1 - train_percentage))

for i in results[:end]:
  if i > 0:
    wins_num += 1
  else:
    lose_num += 1

print(f"Wins: {wins_num}, loose: {lose_num}")

import pickle

with open('q_table_player_1.txt', 'wb') as file:
    pickle.dump(dict(agent.Q), file)

import statistics
print(f"Player expected score was {statistics.fmean(results)}")
pygame.time.wait(3000)
pygame.quit()
