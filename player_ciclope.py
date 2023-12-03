import random

class Player_ciclope:
  def decision(self, your_hand, round_num):
    print("Player current hand", [d for d in your_hand])  
    print(f"Making decision...\n")       

    if round_num < total/2:
        choice = random.choice(["hit", "stop"])
    else:
       pass
    
    print("You made the decision ", choice)
    print("------------------- ", choice)
    return choice

  def result(self, your_hand, decision, reward, is_not_done):
    print("Your hand is ", your_hand)
    print("Reward :", reward, " is_not_done? ", is_not_done)  
    print("==================== ")    
    pass
  