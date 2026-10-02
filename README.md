# Blackjack Reinforcement Learning Agent

This repository contains a Python implementation of a Blackjack agent trained using reinforcement learning (Q-learning). The agent learns an optimal strategy for playing Blackjack by exploring and exploiting a Q-table over multiple rounds.

---

## Dependencies

Make sure you have the following dependencies installed:

- Python 3.x
- NumPy
- Pygame
- Matplotlib

Install the required packages using:

```bash
pip install numpy pygame matplotlib
```

---

## File Overview

| File | Description |
|---|---|
| `blackjack_game.py` | Main script — runs the game loop, manages rounds, and writes results to a file |
| `blackjack_players.py` | Player agent implementations (`Player_simple`, `Player_double`, `Player_master`) |
| `q_table_player.py` | Q-learning agent (`RLAgent`) with Q-table logic |
| `gen_cards.py` | Generates card image assets |
| `plot_results.py` | Reads result files and plots wins, losses, and expected score over executions |
| `bash.sh` | Helper script to run the game multiple times and collect results |

---

## How to Run

Run the main script with 5 positional arguments:

```bash
python3 blackjack_game.py <rounds> <train_percentage> <alpha> <gamma> <epsilon>
```

### Example

```bash
python3 blackjack_game.py 100 0.8 0.5 0.5 0.1
```

---

## Parameters

| Parameter | Position | Type | Example | Description |
|---|---|---|---|---|
| `rounds` | 1st | `int` | `100` | Total number of rounds to play |
| `train_percentage` | 2nd | `float` | `0.8` | Fraction of rounds used for **training** (random exploration). The remaining rounds are used for **testing** (exploiting the learned Q-table). |
| `alpha` | 3rd | `float` | `0.5` | **Learning rate** — controls how much new information overwrites old Q-table values. Higher values make the agent learn faster but less stably. |
| `gamma` | 4th | `float` | `0.5` | **Discount factor** — determines how much future rewards are valued compared to immediate ones. A value of `1.0` gives full weight to future rewards. |
| `epsilon` | 5th | `float` | `0.1` | **Exploration rate** — probability of choosing a random action instead of the best known one. Higher values encourage more exploration. |

---

## Training and Testing

The total number of rounds is split into two phases:

- **Training phase**: The first `rounds × train_percentage` rounds. The agent plays randomly, exploring different actions and updating its Q-table.
- **Testing phase**: The remaining rounds. The agent uses the Q-table it built during training to make decisions.

Results (wins, losses, and expected score) are appended to `results_master.txt` after each run.

---

## Plotting Results

After running the game (preferably multiple times via `bash.sh`), you can visualize the results:

```bash
python3 plot_results.py
```

This will generate plots for `results_simple.txt`, `results_double.txt`, and `results_master.txt`, showing wins, losses, and expected score per execution.

---

## Running Multiple Times (bash.sh)

The `bash.sh` script runs the game 100 times automatically and records all results:

```bash
bash bash.sh
```

You can edit the script to change the number of executions or the parameters passed to `blackjack_game.py`.

---

## Player Agents

Three player strategies are implemented in `blackjack_players.py`:

- **`Player_simple`** — Makes decisions based only on the player's own hand value.
- **`Player_double`** — Makes decisions based on both the player's hand and the dealer's visible card.
- **`Player_master`** — Uses a basic Blackjack strategy combined with the Q-learning agent for edge cases.

The active player is set in `blackjack_game.py` (line 139).
