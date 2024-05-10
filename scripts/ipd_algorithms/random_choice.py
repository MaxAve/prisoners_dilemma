import random
import prisoners_dilemma as ipd

def get_choice(game_history, player_num):
    return ipd.COOPERATE if random.randint(0, 1) == 0 else ipd.STEAL