import pygame, random, itertools, sys, pickle, statistics

from q_table_player import *
from blackjack_players import *

# Initialize Pygame
pygame.init()

# Game window settings
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Simple Blackjack')

portraits = [
  pygame.image.load(f'portrait/jacare.png')
]

dealer_portrait_img = pygame.image.load(f'portrait/dealer.png'),  

winner_image = pygame.transform.scale(pygame.image.load(f'symbols/winner.png'), (200, 200))

# Load card images (assuming we have basic card images named as '2_of_clubs.png', '3_of_hearts.png', etc.)
card_images = {}
suits = ['hearts', 'diamonds', 'clubs', 'spades']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
player_portrait = pygame.transform.scale(random.choice(portraits), (80, 160))
dealer_portrait = pygame.transform.scale(random.choice(dealer_portrait_img), (80, 160))

for suit in suits:
    for value in values:
        image_scale = 0.5
        card_img =  pygame.image.load(f'cards/{value}_of_{suit}.png')
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

class DealerPlayer:
  def decision(self, player_hand, dealer_hand):
    dealer_value = calculate_hand_value(dealer_hand)
    if dealer_value < 17:
      return "hit"
    else:
      return "stop"

  def result(self, player_hand, dealer_hand, decision, reward, is_not_done):
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

        screen.fill((0, 0, 0))  # Clear screen (black background)

        if dealer_turn:
            # Dealer's turn logic
            dealer_value = calculate_hand_value(dealer_hand)
            if dealer_value < 17:
                draw_card(deck, dealer_hand) 
            else:
              dealer_turn = False
              player_turn = True       
        elif player_turn:

            decision = player.decision(player_hand, dealer_hand, round_num, total_rounds)
            if decision == "hit":
              draw_card(deck, player_hand)
            else:
              player_turn = False

            if calculate_hand_value(player_hand) >= 21:
              player_turn = False                
               
            if not player_turn:         
              player_value = calculate_hand_value(player_hand)
              reward = player.result(player_value, dealer_value, player_turn) # Compare hands and decide winner
              
              hand_result = reward

              print(f"Round result {hand_result}")                     
              running = False
            
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

    return hand_result

player = Player_master()

results = []
total_rounds = int(sys.argv[1])
train_percentage = float(sys.argv[2])

wins_num = lose_num = 0

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

print(f"Player expected score was {statistics.fmean(results)}")
pygame.time.wait(3000)
pygame.quit()
