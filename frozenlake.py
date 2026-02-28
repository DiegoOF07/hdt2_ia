import numpy as np
from mdp import MDP


class FrozenLakeMDP(MDP):
    
    def __init__(self, grid_file, gamma=0.9):
        
        self.grid = self.load_grid(grid_file)
        self.n_rows = len(self.grid)
        self.n_cols = len(self.grid[0])
        self.n_states = self.n_rows * self.n_cols
        self.n_actions = 4
        super().__init__(self.n_states, self.n_actions, gamma)
        
        # Acciones
        self.actions = {
            0: (-1, 0), #Norte
            1: (1, 0), #Sur
            2: (0, 1), #Este
            3: (0, -1) #Oeste
        }
        
        self.n_actions = 4
        
    def load_grid(self, filename):
        grid = []
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    grid.append(list(line))
        return grid
    
    def state_to_pos(self, state):
        return divmod(state, self.n_cols)
    
    def pos_to_state(self, row, col):
        return row * self.n_cols + col
    
    def is_terminal(self, state):
        row, col = self.state_to_pos(state)
        return self.grid[row][col] in ['H', 'G']
    
    def move(self, state, action):
        row, col = self.state_to_pos(state)
        dr, dc = self.actions[action]
        
        new_row = min(max(row + dr, 0), self.n_rows - 1)
        new_col = min(max(col + dc, 0), self.n_cols - 1)
        
        return self.pos_to_state(new_row, new_col)
    
    def get_transitions(self, state, action):
        
        if self.is_terminal(state):
            return [(1.0, state)]
        
        # Acciones perpendiculares
        if action in [0,1]:
            perpendicular = [2,3]
        else:
            perpendicular = [0,1]
            
        possible_actions = [action] + perpendicular
        transitions = []
    
        for a in possible_actions:
            next_state = self.move(state, a)
            transitions.append((1/3, next_state))
        
        return transitions
    
    def reward(self, state, action, next_state):
        row, col = self.state_to_pos(next_state)
        cell = self.grid[row][col]
        
        if cell == 'G':
            return 1.0
        else:
            return 0.0