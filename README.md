**Blackjack Reinforcement Learning Agent**

This repository contains a Python implementation of a Blackjack agent trained using reinforcement learning. The agent uses the Q-learning algorithm to learn an optimal strategy for playing Blackjack.

### Dependencies

Make sure you have the following dependencies installed:

- Python 3.x
- NumPy
- Pygame (for visualization purposes)

Install the required packages using:


### Running the Code

Run the `blackjack_rl.py` file to train and test the Blackjack reinforcement learning agent. The agent's Q-table is saved to and loaded from a file (`q_table_player.txt`) using the `pickle` module.

### Code Overview

- `blackjack_game.py`: Main script for training and testing the reinforcement learning agent.
- `blackjack_players.py`: Implementation of the Blackjack reinforcement learning agents.
- `q_table_player.py`: Implementation of q-table logic.
- `gen_cards.py`: Implementation of the cards printing logic.

### Running

You can adjust the learning parameters in the execution moment. Parameters include:

- Number of rounds, percentage for training, alpha, gamma, epsilon. (1000 0.9 0.5 0.5 0.2)
- Learning rate (`alpha`): Controls the impact of new information on the agent's knowledge.
- Discount factor (`gamma`): Determines the importance of future rewards.
- Exploration rate (`epsilon`): Probability of taking a random action instead of the optimal one.

### Training and Testing

The agent is trained through the number of rounds multiplied by the percentage of training, the rounds that last are used for testing.

### Note

Ensure that you have the required dependencies installed, and feel free to customize the code to experiment with different parameters or enhance the learning algorithm.

Feel free to reach out if you have any questions or need further clarification on the code!
