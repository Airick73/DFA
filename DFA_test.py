import unittest
from DFA import DFA

class TestDFA(unittest.TestCase):
    
    def setUp(self):
        Q = {0,1,2}
        Sigma = {"a","b"}
        delta = {
            (0, "a") : 0,
            (0, "b") : 1,
            (1, "a") : 2,
            (1, "b") : 1, 
            (2, "a") : 2,
            (2, "b") : 2
        }
        q0 = 0
        F = {0,1}
        self.A_B4_B_DFA = DFA(Q, Sigma, delta, q0, F)

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
        self.Odd_or_Even_DFA = DFA(Q, Sigma, delta, q0, F)

        Q = {0,1}
        Sigma = {"a","b"}
        delta = {
                    (0, "a") : 1,
                    (1, "a") : 0,
                    (0, "b") : 1,
                    (1, "b") : 0
                }
        q0 = 0
        F = {0}
        self.Pre_minimized_Odd_or_Even_DFA = DFA(Q, Sigma, delta, q0, F)
    
    def test_valid_sequnces_DFA(self):
        self.assertEqual(self.A_B4_B_DFA.run("a"), True)
        self.assertEqual(self.A_B4_B_DFA.run("b"), True)
        self.assertEqual(self.A_B4_B_DFA.run("bbbb"), True)
        self.assertEqual(self.A_B4_B_DFA.run("ab"), True)
        self.assertEqual(self.A_B4_B_DFA.run("aaa"), True)
        self.assertEqual(self.A_B4_B_DFA.run("aaabbb"), True)
        self.assertEqual(self.A_B4_B_DFA.run(""), True)

    def test_invalid_sequnces_A_B4_B_DFA(self):
        self.assertEqual(self.A_B4_B_DFA.run("ba"), False)
        self.assertEqual(self.A_B4_B_DFA.run("bba"), False)
        self.assertEqual(self.A_B4_B_DFA.run("aba"), False)
        self.assertEqual(self.A_B4_B_DFA.run("abab"), False)

    def test_valid_sequnces_Odd_or_Even_DFA(self):
        self.assertEqual(self.Odd_or_Even_DFA.run(""), True)
        self.assertEqual(self.Odd_or_Even_DFA.run("aa"), True)
        self.assertEqual(self.Odd_or_Even_DFA.run("ab"), True)
        self.assertEqual(self.Odd_or_Even_DFA.run("bb"), True)
        self.assertEqual(self.Odd_or_Even_DFA.run("aabb"), True)

    def test_invalid_sequnces_Odd_or_Even_DFA(self):
        self.assertEqual(self.Odd_or_Even_DFA.run("a"), False)
        self.assertEqual(self.Odd_or_Even_DFA.run("abb"), False)
        self.assertEqual(self.Odd_or_Even_DFA.run("aaa"), False)

    def test_valid_sequnces_Pre_minimized_Odd_or_Even_DFA(self):
        self.assertEqual(self.Pre_minimized_Odd_or_Even_DFA.run(""), True)
        self.assertEqual(self.Pre_minimized_Odd_or_Even_DFA.run("aa"), True)
        self.assertEqual(self.Pre_minimized_Odd_or_Even_DFA.run("ab"), True)
        self.assertEqual(self.Pre_minimized_Odd_or_Even_DFA.run("bb"), True)
        self.assertEqual(self.Pre_minimized_Odd_or_Even_DFA.run("aabb"), True)

    def test_invalid_sequnces_Pre_minimized_Odd_or_Even_DFA(self):
        self.assertEqual(self.Pre_minimized_Odd_or_Even_DFA.run("a"), False)
        self.assertEqual(self.Pre_minimized_Odd_or_Even_DFA.run("abb"), False)
        self.assertEqual(self.Pre_minimized_Odd_or_Even_DFA.run("aaa"), False)

    def test_minimize_Odd_or_Even_DFA(self):
        minimized_odd_or_even_DFA = self.Odd_or_Even_DFA.minimize()
        self.assertEqual(len(minimized_odd_or_even_DFA.Q), 2)
        self.assertEqual(minimized_odd_or_even_DFA.F, {0,1})

if __name__ == '__main__':
    unittest.main()

        