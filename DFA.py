class DFA:
    def __init__(self, Q, Sigma, delta, q0, F):
        """
        Q: Set of states.
        Sigma: Alphabet.
        delta: Transition function (dictionary).
        q0: Initial state.
        F: Set of final states.
        """
        self.Q = Q
        self.Sigma = Sigma
        self.delta = delta 
        self.q0 = q0    
        self.F = F

    def run(self, word):        
        """
        Simulates the DFA on the input word.
        Returns True if word is accepted, otherwise False.
        """
        q = self.q0
        while word != "":
            q = self.delta[(q, word[0])]
            word = word[1:]
        return q in self.F
    
    def minimize(self):
        """
        Minimizes the DFA using the table filling algorithm.
        Returns a new minimized DFA.
        """
        states = list(self.Q)
        distinct_table = {}
        state_pairs = set()

        # create unique state pairs 
        for i in range(len(self.Q)):
            for j in range(i + 1, len(self.Q)):
                state_one = states[i]
                state_two = states[j]
                state_pairs.add((state_one, state_two))

        # number of unqiue states should be == n (n - 1) / 2
        assert( len(state_pairs) == (len(states) * (len(states) - 1) / 2) )

        # initialize distinguishability table
        for state_pair in state_pairs:
            if (state_pair[0] in self.F) != (state_pair[1] in self.F):
                distinct_table[state_pair] = True
            else:
                distinct_table[state_pair] = False

        # Loop through unmarked pairs in table until a marking can no longer be made 
        while True:
            marking_occured = False
            
            for state_pair in distinct_table:
                for input_symbol in self.Sigma:
                    state_one = self.delta[(state_pair[0], input_symbol)]
                    state_two = self.delta[(state_pair[1], input_symbol)]
                    
                    check_pair = tuple(sorted((state_one, state_two)))
                    
                    if distinct_table.get(check_pair, False) and distinct_table[state_pair] == False:
                        distinct_table[state_pair] = True
                        marking_occured = True
                    
            if marking_occured == False:
                break
                
        indistinct_state_pairs = [state_pair for state_pair, is_distinct in distinct_table.items() if is_distinct == False]

        # Create new delta with merged states from indistinguisable states
        new_delta = {}
        
        for (state, action), next_state in self.delta.items():
            for indistinct_state_pair in indistinct_state_pairs:
                if state in indistinct_state_pair:
                    state = indistinct_state_pair
                if next_state in indistinct_state_pair:
                    next_state = indistinct_state_pair
            new_delta[(state, action)] = next_state 

        new_Q = list(self.Q)
        new_q0 = 0
        new_F = list(self.F)
        for state in list(self.Q):
            for indistinct_state_pair in indistinct_state_pairs:
                if state in indistinct_state_pair:
                    new_Q.remove(state)
                    new_Q.append(indistinct_state_pair)
                if new_q0 in indistinct_state_pair:
                    new_q0 = indistinct_state_pair

        for state in list(self.F):
            for indistinct_state_pair in indistinct_state_pairs:
                if state in indistinct_state_pair:
                    new_F.remove(state)
                    new_F.append(indistinct_state_pair)
        
        new_Q = set(new_Q)
        new_F = set(new_F)

        return DFA(new_Q, self.Sigma, new_delta, new_q0, new_F)        
