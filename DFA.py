import copy 

class DFA:
    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q
        self.Sigma = Sigma
        self.delta = delta 
        self.q0 = q0    
        self.F = F

    def run(self, word):
        q = self.q0
        while word != "":
            q = self.delta[(q, word[0])]
            word = word[1:]
        return q in self.F
    
    def minimize(self):
        final_states = list(self.F)
        non_final_states = [state for state in self.Q if state not in self.F]
        states = list(self.Q)
        distinct_table = {}
        state_pairs = set()

        # create unique state pairs 
        for i in range(len(self.Q)):
            for j in range(i + 1, len(self.Q)):
                P = states[i]
                Q = states[j]
                state_pairs.add((P,Q))

        # number of unqiue states should be == n (n - 1) / 2
        assert( len(state_pairs) == (len(states) * (len(states) - 1) / 2) )

        for state_pair in state_pairs:
            if state_pair[0] in self.F and state_pair[1] not in self.F or\
                state_pair[0] not in self.F and state_pair[1] in self.F:
                
                distinct_table[state_pair] = True
            
            else:
                
                distinct_table[state_pair] = False

        while True:
            marking_occured = False
            
            for state_pair in distinct_table:
                for input_symbol in self.Sigma:
                    state_one = self.delta[(state_pair[0], input_symbol)]
                    state_two = self.delta[(state_pair[1], input_symbol)]
                    
                    # checking pair in acsending order 
                    if state_one < state_two:
                        check_pair = (state_one, state_two)
                    else:
                        check_pair = (state_two, state_one)

                    if distinct_table[check_pair] and distinct_table[state_pair] == False:
                        distinct_table[state_pair] = True
                        marking_occured = True
                    
            if marking_occured == False:
                break
                
        indistinct_state_pairs = [state_pair for state_pair, is_distinct in distinct_table.items() if is_distinct == False]

        # given a set {0,1,2,3} 
        # given a list of tuples [(0,3), (1,2)]
        # make a set out of the states which appear in the tuple 

        # Make a mapping of old states to new states 
        new_delta = copy.copy(self.delta)
        for state_action_pair in new_delta:
            for indistinct_state_pair in indistinct_state_pairs:
                if new_delta[state_action_pair] in indistinct_state_pair:
                     new_delta[state_action_pair] = indistinct_state_pair

        


        # return minimal DFA
        pass
        
    
Q = {0,1,2,3}
Sigma = {"a","b"}
delta = {
    (0, "a") : 1,
    (0, "b") : 2,
    (1, "a") : 0,
    (1, "b") : 3, 
    (2, "a") : 3,
    (2, "b") : 0,
    (3, "a") : 2,
    (3, "b") : 1
}
q0 = 0
F = {0,3}
Odd_or_Even_DFA = DFA(Q, Sigma, delta, q0, F)
Odd_or_Even_DFA.minimize()
