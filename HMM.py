# -*- coding: utf-8 -*-
"""
Course: DSCI552
Assignment 7 HMM
@author: Li An, Shengnan Ke
"""


class HMM:
    def __init__(self, evids):
        self.T = len(evids)  # total number of states
        self.evids = evids  # evidence variables
        self.domain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # all the possible squences and their probabilities
        self.probs = []
        self.sequences = []

    def run_Viterbi(self):
        init_prob = 0.1
        em_prob = 1 / 3
        
        # find all possible sequences and their probabilities
        for v1 in self.domain:  # possible value of x1 according to e1
            if self.evids[0] in (v1-1, v1, v1+1):
                # print('here',v1,self.evids[0])
                self.explore(sequence=[v1], prob=init_prob * em_prob, idx_t=1)  # add v1 to sequence, explore remaining x
        
        # return the sequence with the highest probability
        max_prob = 0
        max_idx = 0
        for i, prob in enumerate(self.probs):
            if prob > max_prob:
                max_idx = i
                max_prob = prob
        result = self.sequences[max_idx]
        if max_prob == 0:
            print('Can\'t find a valid solution!')
        else:
            print('The most likely sequence of values v1 v2 ... v10: ')
            print(result)
        
    
    # sequence: values of variables which have already been confirmed
    # prob: probability of sequence
    # idx_t: index of the last variable in the sequence
    def explore(self, sequence, prob, idx_t):
        # Found a complete assignment of variables, end the recursion
        if idx_t == self.T:
            self.probs.append(prob)
            self.sequences.append(sequence)
            return
        
        prev_state = sequence[-1]

        # Transition probabilities
        if prev_state == 1:
            trans_prob = [(2, 1.0),]
        elif prev_state == 10:
            trans_prob = [(9, 1.0),]
        else:
            trans_prob = [(prev_state - 1, 0.5), (prev_state + 1, 0.5)]

        # Find possible values of the next variable
        for state, p in trans_prob:
            if self.evids[idx_t] in (state-1, state, state+1):
                sequence.append(state)
                self.explore(sequence=sequence, prob=prob * p, idx_t=idx_t + 1)


if __name__ == "__main__":
    observations = [8, 6, 4, 6, 5, 4, 5, 5, 7, 9]
    hmm = HMM(observations)
    hmm.run_Viterbi()