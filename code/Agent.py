
from abc import ABC, abstractmethod


class Agent(ABC) :
    def __init__(self) -> None:
        self.played_round=0
        
    @abstractmethod
    def choose_action(self,state,possible_actions):
        pass

    @abstractmethod
    def update(self,state,action,reward,next_state):
        pass
    
    