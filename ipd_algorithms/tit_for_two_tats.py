import prisoners_dilemma as ipd

def get_choice(game_history, player_num):
    if len(game_history) > 1:
        # Will steal only if the opponent stole 2x in a row
        return game_history[-1][0 if player_num == 1 else 1] or game_history[-2][0 if player_num == 1 else 1]
    else:
        return ipd.COOPERATE # Always cooperate on the first round
    
def next_round(round_number):
    pass