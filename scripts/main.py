import random
import prisoners_dilemma as ipd

from ipd_algorithms import random_choice
from ipd_algorithms import tit_for_tat
from ipd_algorithms import tit_for_two_tats

# Plays a round between 2 algorithms (modules with a get_choice() function)
def submit_round(game, p1_algorithm, p2_algorithm):
    game.submit_round(p1_algorithm.get_choice(game.game, 0), p2_algorithm.get_choice(game.game, 1))

def main():
    game = ipd.Game()
    game.set_noise(5)
    for i in range(50):
        submit_round(game, tit_for_two_tats, tit_for_tat)
    print(game)

if __name__ == "__main__":
    main()