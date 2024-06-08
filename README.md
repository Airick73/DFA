# DFA Library 

This repository provides a Python implementation of a Deterministic Finite Automaton (DFA) and includes functionality to minimize the DFA using the table filling algorithm. Additionally, it includes a test suite to validate the correctness of the DFA operations.

## Files

- `DFA.py`: Contains the `DFA` class, which implements a DFA and its minimization.
- `test_DFA.py`: Contains unit tests for the `DFA` class.

## DFA Class

### Initialization

```python
"""
Q: Set of states.
Sigma: Alphabet.
delta: Transition function (dictionary).
q0: Initial state.
F: Set of final states.
"""
def __init__(self, Q, Sigma, delta, q0, F):
    self.Q = Q
    self.Sigma = Sigma
    self.delta = delta 
    self.q0 = q0    
    self.F = F
```

### Methods 
## run()
```python
"""
Simulates the DFA on the input word.
Returns True if word is accepted, otherwise False.
"""
def run(self, word):
    q = self.q0
    while word != "":
        q = self.delta[(q, word[0])]
        word = word[1:]
    return q in self.F
```
## minimize()
```python
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
```
### Usage 
## Running the DFA
```python
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
dfa = DFA(Q, Sigma, delta, q0, F)
print(dfa.run("aabb"))  # Example usage
minimized_dfa = dfa.minimize()
```
### Testing 
## Running Tests
```python
python -m unittest test_DFA.py
```
## Test Cases 
- Valid sequences for different DFAs.
- Invalid sequences for different DFAs.
- Testing the minimization process.

### References 
[1] Simplified DFA Minimization - Computerphile, YouTube, uploaded by Computerphile, 9 May 2017, [Simplified DFA Minimization - Computerphile](https://www.youtube.com/watch?v=oHVHkkah3MY&list=PLzH6n4zXuckpc5x08oRM4AI02g5KwFQov&index=2&pp=iAQB)





