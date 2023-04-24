from code import Agent
from code.Agents.RandomAgent import RandomAgent
from code.Grid import Grid


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

  def play_round(self,action:int):
      """function_agent : fonction de choix de l'agent"""
      reward=-1
      #action=np.random.randint(0,4)
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


  def play_game(self,agent,stop=100000, print_game=False,train=True)->bool:
      print("Let start a new game")
      while not self.end:
          state=self.grid.state.copy()
          action = agent.choose_action(
             state,
             self.grid.get_possible_actions()
          )
          reward,next_state,action=self.play_round(action)

          if train:agent.update(state, action, reward, next_state)
          self.sum_reward+=reward
          if self.round > stop:
            return False
            break
          self.round+=1
          if print_game :print(self)
      return True

  def __str__(self):
      game_to_show=f"---- {self.round} ----------\n"
      game_to_show+=self.grid.__str__()
      game_to_show+=f"\nReward Round: {self.reward} \nReward cum: {self.sum_reward}"
      return game_to_show