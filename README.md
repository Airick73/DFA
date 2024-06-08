# DFA Minimization Repository

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
"""
Minimizes the DFA using the table filling algorithm.
Returns a new minimized DFA.
"""
def minimize(self):
    # Minimization logic here...
    pass
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




