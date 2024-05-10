import prisoners_dilemma as ipd

def get_choice(game_history, player_num):
    if len(game_history) >= 1:
        return game_history[-1][0 if player_num == 1 else 1] # Do whatever the opponent did in the last round
    else:
        return ipd.COOPERATE # Always cooperate on the first round