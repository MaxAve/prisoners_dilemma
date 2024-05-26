import random
import prisoners_dilemma as ipd

import os
os.system("clear")

# Import different algorithms for solving an Iterative Prisoner's Dilemma (IPD)
from ipd_algorithms import random_choice, tit_for_tat, tit_for_two_tats, neural_network, grim_trigger, sneaky

# Plays a round between 2 algorithms (modules with a get_choice() function)
def submit_round(game, round_number,  p1_algorithm, p2_algorithm):
    game.submit_round(p1_algorithm.get_choice(game.game, 0), p2_algorithm.get_choice(game.game, 1))

def main():
    algorithm1 = sneaky
    algorithm2 = sneaky

    for i in range(10):
        print("Starting next round...")
        game = ipd.Game()
        game.set_noise(0)
        for i in range(50):
            submit_round(game, i, algorithm1, algorithm2)
        print(game) 
        algorithm1.next_round(i)
        algorithm2.next_round(i)

if __name__ == "__main__":
    main()