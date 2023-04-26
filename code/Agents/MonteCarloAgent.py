import numpy as np
from code.Agent import Agent


class MonteCarloAgent(Agent):
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.1, size=1):
        super().__init__()
        self.Q = {}
        self.N = {}#Dict to count the number of occurence of  first-visited  for each state throught multiple episodes
        self.sum_G= {}
        self.actions = [0, 1, 2, 3]
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.size = size ** 2

    def choose_action(self, state, possible_actions):
        self.played_round += 1
        if np.random.uniform() < self.epsilon:
            return np.random.choice(possible_actions)
        else:
            # Choose the action with the highest Q-value
            q_values = [self.Q.get((tuple(state.reshape(self.size)), a), 0) for a in possible_actions]
            max_q = max(q_values)
            if q_values.count(max_q) > 1:
                # Multiple actions have the same highest Q-value, choose one randomly
                return possible_actions[np.random.choice(np.flatnonzero(np.array(q_values) == np.array(q_values).max()))]
            else:
                return possible_actions[np.argmax(q_values)]
    



    def update(self, state, action, reward, next_state,next_action):
        pass


    def update_episode(self, episode):
        states_visited = set()
        for i, (reward, state,action) in enumerate(episode):
            state = tuple(state.reshape(self.size))
            # First visited MC
            if state not in states_visited:
                states_visited.add(state)
                G = sum([r * (self.gamma ** j) for j, (_, _, r) in enumerate(episode[i:])])
                self.N[state,action]=self.N.get((state,action),0)+1
                print('updated')
                self.sum_G[state,action]=self.sum_G.get((state,action),0)+G
                self.Q[state,action]=self.sum_G[state,action]/self.N[state,action]# add G
