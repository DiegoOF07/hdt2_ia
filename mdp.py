import numpy as np

class MDP:
    
    def __init__(self, n_states, n_actions, gamma=0.9):
        self.n_states = n_states
        self.n_actions = n_actions
        self.gamma = gamma
    
    def get_transitions(self, state, action):
        raise NotImplementedError
    
    def reward(self, state, action, next_state):
        raise NotImplementedError
    
    def is_terminal(self, state):
        raise NotImplementedError