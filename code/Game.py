from code.Grid import Grid
from code.Agent import Agent

import numpy as np

class Game:
  
  def __init__(self,size=2) -> None:
      self.grid=Grid(size)

      self.end=False
      self.round=0
      self.reward=0
      self.sum_reward=0
      self.actions=[]# list of all actions done in the game
      self.last_good=0
      self.number_good_place=0
      self.all_grid=[]

  def play_round(self,action):
      """function_agent : fonction de choix de l'agent"""
      reward=-1


      self.grid.take_action(action)
      if self.grid.is_finish():
        self.end = True
        reward += 50000

      if self.grid.get_good_place() == self.number_good_place + 1:
        reward += 100
        self.last_good += 1
        self.number_good_place += 1
      elif self.grid.get_good_place() <= self.number_good_place:
        reward -= 10

      return reward,self.grid.state,action


  def play_game(self,agent:Agent,stop=100000, print_game=False,train=True)->bool:

      if agent.__class__.__name__ == 'SarsaAgent':
          agent.prev_state = None
          agent.prev_action = None
      episode=[]

      
      while not self.end:
          state=self.grid.state.copy()
          action = agent.choose_action(
             state,
             self.grid.get_possible_actions()
          )

          reward,next_state,action=self.play_round(action)
          next_action = agent.choose_action(next_state, self.grid.get_possible_actions())
          episode.append((reward,state,action))
          if train:
              agent.update(state, action, reward, next_state, next_action)               
          self.sum_reward+=reward
          self.round+=1
          if print_game :
             print(self)
             self.all_grid.append(state)
          if self.round >= stop:
            return False
            
      self.end=True
      if train: agent.update_episode(episode=episode)
        
      return True

  def __str__(self):
      game_to_show=f"---- {self.round} ----------\n"
      game_to_show+=self.grid.__str__()
      game_to_show+=f"\nReward Round: {self.reward} \nReward cum: {self.sum_reward}"
      return game_to_show