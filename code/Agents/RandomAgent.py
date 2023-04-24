
import random
from code.Agent import Agent


class RandomAgent(Agent):
    def __init__(self) -> None:
        super().__init__()
    
    def choose_action(self,state, possible_actions):
        self.played_round+=1
        return random.choice(possible_actions)

    def update(self,state, action, reward, next_state):
        #Do nothing
        pass