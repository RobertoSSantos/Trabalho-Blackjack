from collections import defaultdict
import numpy as np
import os, pickle, pygame, sys

class RLAgent:
  def __init__(self):
  
    self.alpha = float(sys.argv[3]) # Learning rate
    self.gamma = float(sys.argv[4]) # Discount factor
    self.epsilon = float(sys.argv[5]) # Exploration rate
    
    self.last_opponent_action = None # Lembrando a ultima acao  
    self.last_round = False # Flag indicando se essa seria a ultima rodada   
       
    #q_table_file = 'q_table_player.pkl' # Q table
    # if os.path.exists(q_table_file) and os.path.getsize(q_table_file) > 0:
    #   with open(q_table_file, 'rb') as file:
    #     print("Using pre-trained q-table!")
    #     self.Q = pickle.load(file)
    # else:

    print("Using a new q-table!")
    self.Q = defaultdict(lambda: [0.0, 0.0])

    pygame.time.wait(3000)     

    self.action_list = ["hit", "stop"]
    self.current_output = None    
 
  def choose_action(self, state):
    if np.random.uniform(0, 1) < self.epsilon:     
      action = np.random.choice(self.action_list) # Explore: Choose a random action
    else:  
      action = self.action_list[np.argmax(self.Q[state])] # Exploit: Choose the action with the maximum Q-value
    return action
    
  def update_qtable(self, state, action, reward, next_state):
    alp = self.alpha
    gam = self.gamma
    action_index = self.action_list.index(action)
    self.Q[state][action_index] = (1 - alp) * self.Q[state][action_index] + alp * (reward + gam * np.max(self.Q[next_state]))  
    
  def get_name(self): # Nome de seu agente deve ser colocado aqui
    return "Giulia Franca"

  def decision(self, player_value):
    print(f"{player_value=} {self.Q=}")

    return self.choose_action(player_value)
    