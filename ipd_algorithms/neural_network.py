import os
import torch
import prisoners_dilemma as ipd
from torch import nn

GENERATION_SIZE = 10 # Number of agents present in every generation

# Convert an action (steal or cooperate) into a numerical value (steal = -1, coop. = 1)
def tokenize_action(action) -> float:
    return 1.0 if action else -1.0

# PyTorch model
class NeuralNetwork(nn.Module):
    def __init__(self, memory):
        super().__init__()
        self.mem_len = memory # Amount of recent actions the network will take into account when evaluating
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(self.mem_len, 8, dtype=torch.float32),
            nn.ReLU(),
            nn.Linear(8, 8, dtype=torch.float32),
            nn.ReLU(),
            nn.Linear(8, 2, dtype=torch.float32) # The first output value is the network's evaluation for cooperating; the second for stealing
        )

    def forward(self, x):
        x = x.to(torch.float32)
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits
    
    # Tokenizes the latest action history from the opponent and returns it as a tensor
    def tokenize(self, game_history, player_num):
        data = []
        if len(game_history) < self.mem_len/2:
            data = [1.0] * (int(self.mem_len) - len(game_history)) # To fill the missing actions during the start, the network will assume the opponent means no harm
            for action in game_history:
                data.append(tokenize_action(action[0 if player_num == 1 else 1]))
        else:
            for i in range(int(self.mem_len)):
                action = game_history[len(game_history) - 1 - i]
                data.append(tokenize_action(action[0 if player_num == 1 else 1]))
        return torch.tensor([[data]])

print(f"[{__name__}]: Initializing neural networks...")
# Create the first generation of agents
generation = []
working_agent = 0 # Index of the current active agent
for i in range(GENERATION_SIZE):
    generation.append(NeuralNetwork(5))

# Cross-breeds surviving agents
def next_generation():
    global working_agent
    working_agent = 0

# Returns network's choice
def get_choice(game_history, player_num):
    global working_agent
    # Result as a list of 2 elements representing the evaluation of cooperating and stealing respectively
    res = generation[working_agent].forward(generation[working_agent].tokenize(game_history, player_num)).tolist()[0]
    #print(res)
    return ipd.COOPERATE if res[0] > res[1] else ipd.STEAL

def next_round(round_number):
    global working_agent
    working_agent += 1
    if working_agent >= len(generation):
        print(f"[{__name__}]: Spawning next generation...")
        next_generation()