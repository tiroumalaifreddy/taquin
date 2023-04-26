import numpy as np
from code.Agent import Agent


class QLearningAgent(Agent):
    def __init__(self,alpha=0.1,gamma=0.9,epsilon=0.1,size=1) -> None:
        super().__init__()
        self.Q = {}
        self.actions = [0,1,2,3]
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.size=size**2
    
    def get_Q(self, state, action):
        if tuple(state.reshape(self.size)) not in self.Q:
            self.Q[tuple(state.reshape(self.size))] = np.zeros(len(self.actions))
        return self.Q[tuple(state.reshape(self.size))][action]
    
    def choose_action(self,state, possible_actions):
        self.played_round+=1
        if np.random.uniform() < self.epsilon:
            return np.random.choice(possible_actions)
        else:
            # Choose the action with the highest Q-value
            q_values = [self.get_Q(state, a) for a in possible_actions]
            max_q = max(q_values)
            if q_values.count(max_q) > 1:
                # Multiple actions have the same highest Q-value, choose one randomly
                return possible_actions[np.random.choice(np.flatnonzero(np.array(q_values) == np.array(q_values).max()))]
            else:
                return possible_actions[np.argmax(q_values)]

    def update(self,state, action, reward, next_state):
        old_Q = self.get_Q(state, action)
        next_max_Q = max([self.get_Q(next_state, a) for a in self.actions])
        new_Q = old_Q + self.alpha * (reward + self.gamma * next_max_Q - old_Q)
        self.Q[tuple(state.reshape(self.size))][action] = new_Q
    
    def update_episode(self, episode):
        pass


    