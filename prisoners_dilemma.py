import random

COOPERATE = True
STEAL = False

class Game:
    def __init__(self):
        self.game = []
        self.__noise_percentage = 0 # % of cooperations that will randomly turn into steals

    def __str__(self):
        ss = [""] * 4
        for action in self.game:
            if action[0] == COOPERATE and action[1] == COOPERATE:
                ss[0] += "+3 "
                ss[3] += "+3 "
            elif action[0] == STEAL and action[1] == COOPERATE:
                ss[0] += "+5 "
                ss[3] += " 0 "
            elif action[0] == COOPERATE and action[1] == STEAL:
                ss[0] += " 0 "
                ss[3] += "+5 "
            else:
                ss[0] += "+1 "
                ss[3] += "+1 "
            
            ss[1] += "\033[42m  \033[0m " if action[0] == COOPERATE else "\033[41m  \033[0m "
            ss[2] += "\033[42m  \033[0m " if action[1] == COOPERATE else "\033[41m  \033[0m "
        return f"\n    {ss[0]}= {self.count_points()[0]}\nP1: {ss[1]}\n\nP2: {ss[2]}\n    {ss[3]}= {self.count_points()[1]}\n"

    def set_noise(self, noise):
        self.__noise_percentage = min(100, max(0, noise))

    def submit_round(self, p1_action: bool, p2_action: bool):
        # Noise
        if self.__noise_percentage > 0:
            if p1_action == COOPERATE and random.randint(0, 100 / self.__noise_percentage) == 0:
                p1_action = STEAL
            if p2_action == COOPERATE and random.randint(0, 100 / self.__noise_percentage) == 0:
                p2_action = STEAL
        self.game.append([p1_action, p2_action])  

    def count_points(self):
        points = [0, 0]
        for action in self.game:
            if action[0] == COOPERATE and action[1] == COOPERATE:
                points[0] += 3
                points[1] += 3
            elif action[0] == STEAL and action[1] == COOPERATE:
                points[0] += 5
            elif action[0] == COOPERATE and action[1] == STEAL:
                points[1] += 5
            else:
                points[0] += 1
                points[1] += 1
        return points
