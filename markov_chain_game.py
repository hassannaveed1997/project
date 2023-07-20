import numpy as np
import pandas as pd
# we only need to keep track of the number of coins a player has in their turn and the number of coins in the pot
# states: (A = 1, pot = 2)

class MarkovChainGame:
    def __init__(self, A_start, B_start, pot) -> None:
        self.total_coins = A_start+B_start+pot
        self.states = self.create_states(self.total_coins)
        self.a_transition_matrix = self.create_transition_matrix()
        self.b_transition_matrix = self.create_b_transition_matrix()
        self.initial_state = self.create_initial_start_matrix(A_start, pot, self.states)

        # store the possible states in a list
    def create_states(self, total_coins):
        states = [(-1,-1)] # the game end is a state added by default
        for pot_coins in range(0,total_coins+1):
            for a_coins in range(0, total_coins+1-pot_coins):
                states.append((a_coins, pot_coins))
        return states
    
    # create transition matrix for player A
    def create_transition_matrix(self):
        # matrix[i][j] = # state i and probability of transitioning to state j
        self.state_dic = {state: i for i, state in enumerate(self.states)}

        # create transition matrix
        transition_matrix = np.zeros((len(self.states), len(self.states)))
        transition_matrix[0][0] = 1 # the game end state is an absorbing state

        p_1,p_2,p_3, p_456 = 1/6,1/6,1/6,1/2

        # create transition probabilities
        for i in range(1, len(self.states)):
            a_coins, pot_coins = self.states[i]
            transition_matrix[i][i] += p_1
            transition_matrix[i][self.state_dic[(a_coins+pot_coins, 0)]] += p_2
            transition_matrix[i][self.state_dic[(a_coins+pot_coins//2, pot_coins-pot_coins//2)]] += p_3
            if a_coins == 0: # if we are in state A = 0, we might transition to the game end state
                transition_matrix[i][0] += p_456
            else:
                transition_matrix[i][self.state_dic[(a_coins-1,pot_coins+1)]] += p_456

        transition_matrix
        transition_df = pd.DataFrame(transition_matrix, columns=self.states, index=self.states)

        return transition_df
    
    # create initial state for player A
    def create_initial_start_matrix(self, A_start, pot, states):
        # create initial state as a pandas series
        initial_state = np.zeros(len(states))
        initial_state[self.state_dic[(A_start, pot)]] = 1
        initial_state = pd.Series(initial_state, index=states)
        return initial_state
    # create transition matrix for player B (states are still in terms of player A's turns)
    def create_b_transition_matrix(self):
        #transitions for player B can be created by row swapping for player A
        # for example, with 10 coins, state (A= 6,pot =2) for player A is state (B = 2,pot = 2) for player B
        A_to_B = np.zeros((len(self.states), len(self.states)))
        A_to_B[0][0] = 1
        for i in range(1, len(self.states)):
            a_coins, pot = self.states[i]
            b_coins = self.total_coins - a_coins - pot

            A_to_B[i][self.state_dic[(b_coins, pot)]] = 1

        # create b transition matrix
        A_to_B_df = pd.DataFrame(A_to_B, columns=self.states, index=self.states)

        b_transition_matrix = A_to_B_df@ self.a_transition_matrix@ A_to_B_df.T
        return b_transition_matrix
    
    # compute the probabilities of a turn ending in a state
    def compute_probabilities(self, num_runs = 50):
        # compute the probability of ending in a state
        X = (self.a_transition_matrix @ self.b_transition_matrix)
        
        probabilties = [0]
        cum_probabilties = [0]
        current_state = self.initial_state
        for i in range(num_runs):
            current_state = current_state @ X
            probabilties.append(current_state[0]- cum_probabilties[-1])
            cum_probabilties.append(current_state[0])

        return np.array(probabilties)

