# State : Correspond a la grid
# Actions: Dé deplacer :
#0: dé en haut
#1: dé a gauche
#2: dé en bas
#3: dé à droite
import numpy as np
import random
from math import floor

from code.utils.functions import build_line, is_solvable


MIN_SIZE = 2
MAX_SIZE = 10
DEFAULT_SIZE = 4

class Grid :
    def __init__(self,size=DEFAULT_SIZE) -> None:
        assert size>=MIN_SIZE and size <= MAX_SIZE
        self.size=size

        while True:
            grid=list(range(size**2))
            random.shuffle(grid)
            grid=np.asarray(grid).reshape(size, size)
            if is_solvable(grid):
                break
        self.state=grid


    def take_action(self,action):
      i, j = np.where(self.state == 0)
      if len(i) > 0 and len(j) > 0:
        i = i[0]
        j = j[0]
        if action == 0:
            if i > 0:
                self.state[i][j], self.state[i-1][j] = self.state[i-1][j], self.state[i][j]
        elif action == 2:
            if i < self.size-1:
                self.state[i][j], self.state[i+1][j] = self.state[i+1][j], self.state[i][j]
        elif action ==1:
            if j > 0:
                self.state[i][j], self.state[i][j-1] = self.state[i][j-1], self.state[i][j]
        elif action == 3:
            if j < self.size-1:
                self.state[i][j], self.state[i][j+1] = self.state[i][j+1], self.state[i][j]

    def is_finish(self):
        ended_grid=[i for i in range(1,self.size**2)]
        ended_grid.append(0)
        return np.array_equal(
            self.state,
            np.asarray(ended_grid).reshape(self.size,self.size)
            )
    
    def get_possible_actions(self):
        """return the possible actions"""
        actions=[i for i in range(0,4)]
        pos_empty=self.get_empty_position()
        if pos_empty[0]==0 : actions.remove(0)
        elif pos_empty[0]==(self.size-1):
            actions.remove(2)
        if pos_empty[1]==0:actions.remove(1)
        elif pos_empty[1]==(self.size-1):
            actions.remove(3)
        return  actions
    
    def get_empty_position(self)->tuple:
        """Return the position od the tuple"""
        return floor(np.argmin(self.state)/self.size),np.argmin(self.state)%self.size

    def get_good_place(self):
      ended_grid=[i for i in range(1,self.size**2)]
      ended_grid.append(0)
      return (np.asarray(ended_grid).reshape(self.size,self.size) == self.state ).sum()


    def __str__(self) -> str:
        """Renderer"""
        tile_line = np.full(self.size, '─' * 4).tolist()
        horizontal_line = build_line('├', '┤', '┼', tile_line)
        first_horizontal_line = build_line('┌', '┐', '┬', tile_line)
        last_horizontal_line = build_line('└', '┘', '┴', tile_line)
        grid_to_show = first_horizontal_line
        for count, row in enumerate(self.state):
            grid_to_show += '│'
            for tile in row:
                if tile == 0:
                    tile = '  '
                grid_to_show += ' %s │' % '{0:>2}'.format(tile)
            if not count == self.size - 1:
                grid_to_show += horizontal_line
        grid_to_show += last_horizontal_line
        grid_to_show+=f"\n Possible actions: {self.get_possible_actions()}"
        return grid_to_show