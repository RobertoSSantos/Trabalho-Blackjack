import random
from collections import defaultdict
import numpy as np
import os
import pickle
import pygame

class RLAgent:
  def __init__(self):
  
    # Learning rate
    self.alpha = 0.5
    # Discount factor
    self.gamma = 0.9
    # Exploration rate
    self.epsilon = 0.1
    # Lembrando a ultima acao
    self.last_opponent_action = None
    # Flag indicando se essa seria a ultima rodada
    self.last_round = False   
    
    # Q table
    q_table_file = 'q_table_player_1.txt'

    if os.path.exists(q_table_file) and os.path.getsize(q_table_file) > 0:
        with open(q_table_file, 'rb') as file:
            print("SUA TIA TO USANDO FILE")
            self.Q = pickle.load(file)
    else:
        print("me de sua tia imediatamente")
        self.Q = defaultdict(lambda: [0.0, 0.0])

    pygame.time.wait(3000)     

    self.action_list = ["hit", "stop"]
    
    self.current_input = None
    self.current_output = None    
 
  def choose_action(self, state):
    if np.random.uniform(0, 1) < self.epsilon:
      # Explore: Choose a random action
      action = np.random.choice(self.action_list)
    else:
      # Exploit: Choose the action with the maximum Q-value
      action = self.action_list[np.argmax(self.Q[state])]
    return action
    
  def update_qtable(self, state, action, reward, next_state):
    alp = self.alpha
    gam = self.gamma
    action_index = self.action_list.index(action)
    self.Q[state][action_index] = (1 - alp) * self.Q[state][action_index] + alp * (reward + gam * np.max(self.Q[next_state]))  
    
  # Nome de seu agente deve ser colocado aqui  
  def get_name(self):
    return "Giulia Franca"

  def decision(self, player_value):
    print(f"{player_value=}")

    print(self.Q)
    return self.choose_action(player_value)

  # Receba as acoes de cada agente e o reward obtido (vs total possivel)
  def result(self, your_action, his_action, total_possible, reward):
    if self.last_round:
      print("Forgetting last opponent action") # Vamos mudar de agente
      self.last_opponent_action = None;
    else:   
      self.last_opponent_action = his_action;
      print(f"For {self.get_name()=} {self.last_opponent_action=} ")   
    
    if your_action == "steal": 
      reward = +0
    # elif your_action == "steal" and his_action == "split":
    #   reward = +2
    # elif your_action == "split" and his_action == "split":
    #   reward = +1
    elif your_action == "split":
      reward = -1
    self.current_output = (your_action, his_action, total_possible, reward )

    