# (Iterative) Prisoner's Dilemma
The Iterative Prisoner's Dilemma (IPD) is a variation of the original Prisoner's Dilemma - a popular game theory problem where two agents/players can either choose to cooperate or steal/defect. Both players must submit their deisions before seeing what the other has chosen, however, in the IPD variation both players can see the past moves they made and use that to make their next decision. This is a big difference since players have to be strategic in how they act. Defecting may yield a high sum of points but if you constantly defect, the opponent will have no reason to keep cooperating and will also be forced to defect, thus reducing the gain for both. **Check the table below for a list of actions and their outcomes**.
### Possible outcomes:
| Player 1  | Player 2  | Outcome                  |
| --------- | --------- | ------------------------ |
| Cooperate | Cooperate | Both gain +3 points      |
| Defect    | Cooperate | Player 1 gains +5 points |
| Cooperate | Defect    | Player 2 gains +5 points |
| Defect    | Defect    | Both gain +1 point       |
### How to get started
**STEP 1:** Install the repository on your device.
```
git clone https://github.com/MaxAve/prisoners_dilemma.git
```
**STEP 2:** CD into the repo's directory and Run the main script to test out whether the installation worked.
```
cd prisoners_dilemma
python3 main.py
```
**STEP 3:** Create your own algorithms inside the ```ipd_algorithms``` directory. You can use the following code snippet as a template, since you ALWAYS have to have these two functions (or the program will crash):
```py
import prisoners_dilemma as ipd

def get_choice(game_history, player_num):
    # This function is executed every time the algorithm has to make a decision on whether to cooperate or defect. Put your logic in this function.
    # The game_history parameter is a list matrix of bools (e.g. [[True, True], [False, True], [True, False], [False, False] ...]). Every sub-list has to have exactly 2 bool elements that represent the actions taken by you and the opponent.
    # The player_num parameter is an int equal to either 0 or 1, it is used to sort the decisions. E.g. game_history[-1][player_num] returns the previous decision made by your algorithm
    return True # The return value has to be a bool that represents the algorithm's decision (True = cooperate, False = defect/steal)
    
def next_round(round_number):
    # This function is executed at the start of a new round.
    # Use the round_number variable to track the current round number if needed.
    pass
```
**STEP 4:** Use the ```submit_round``` function inside ```main.py``` and put in your algorithm's python module name and another one for it to compete against to see the result.
