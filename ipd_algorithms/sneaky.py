import random
import prisoners_dilemma as ipd

DEFECTION_CHANGE = 20 # % chance of the algorithm defecting at random

SNEAKY = 0
RETALIATION = 1
current_strategy = SNEAKY

def get_choice(game_history, player_num):
    global current_strategy

    if len(game_history) < 3:
        return ipd.COOPERATE # Always cooperate for the first 3 rounds to build trust

    opponent_actions_index = 0 if player_num == 1 else 1

    # Switch to tit-for-tat if the opponent defects 2 times in a row
    if current_strategy == SNEAKY and ((game_history[-1][opponent_actions_index] or game_history[-2][opponent_actions_index]) == ipd.STEAL):
        current_strategy = RETALIATION
    
    # Switch back to sneaky if the opponent cooperated 2 times in a row
    if current_strategy == RETALIATION and ((game_history[-1][opponent_actions_index] and game_history[-2][opponent_actions_index]) == ipd.COOPERATE):
        current_strategy = SNEAKY
    
    if current_strategy == RETALIATION:
        return game_history[-1][opponent_actions_index] # Tit-for-tat

    if game_history[-1][opponent_actions_index] == ipd.STEAL and current_strategy == SNEAKY:
        return ipd.COOPERATE # Cooperate as an apology if opponent starts to defect
    else:
        if random.randint(0, 100 / DEFECTION_CHANGE) == 0:
            return ipd.STEAL
        return ipd.COOPERATE
    
def next_round(round_number):
    global current_strategy
    current_strategy = SNEAKY