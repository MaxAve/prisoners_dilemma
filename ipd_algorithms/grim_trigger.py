import prisoners_dilemma as ipd

trigger = ipd.COOPERATE

def get_choice(game_history, player_num):
    global trigger
    if len(game_history) < 1:
        return ipd.COOPERATE # Cooperate in the first round
    if game_history[-1][0 if player_num == 1 else 1] == ipd.STEAL:
        trigger = ipd.STEAL # Always defect after a single defection from opponent
    return trigger
    
def next_round(round_number):
    global trigger
    trigger = ipd.COOPERATE