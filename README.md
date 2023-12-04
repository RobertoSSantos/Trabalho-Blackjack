**Blackjack Reinforcement Learning Agent**

This repository contains a Python implementation of a Blackjack agent trained using reinforcement learning. The agent uses the Q-learning algorithm to learn an optimal strategy for playing Blackjack. The Q-table is stored and loaded using the `pickle` module.

### Dependencies

Make sure you have the following dependencies installed:

- Python 3.x
- NumPy
- Pygame (for visualization purposes)

Install the required packages using:


### Running the Code

Run the `blackjack_rl.py` file to train and test the Blackjack reinforcement learning agent. The agent's Q-table is saved to and loaded from a file (`q_table_player.txt`) using the `pickle` module.


### Code Overview

- `blackjack_rl.py`: Main script for training and testing the reinforcement learning agent.
- `RLAgent.py`: Implementation of the Blackjack reinforcement learning agent (`RLAgent` class).
- `q_table_player.txt`: File to store the Q-table.

### Configuration

You can adjust the learning parameters in the `RLAgent` class in `RLAgent.py`. Parameters include:

- Learning rate (`alpha`): Controls the impact of new information on the agent's knowledge.
- Discount factor (`gamma`): Determines the importance of future rewards.
- Exploration rate (`epsilon`): Probability of taking a random action instead of the optimal one.

### Training and Testing

The agent is trained through episodes of Blackjack, and the learned Q-table is stored in `q_table_player.txt`. After training, the agent can be tested to evaluate its performance.

### Note

Ensure that you have the required dependencies installed, and feel free to customize the code to experiment with different parameters or enhance the learning algorithm.

Feel free to reach out if you have any questions or need further clarification on the code!
