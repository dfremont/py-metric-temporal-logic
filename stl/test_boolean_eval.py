import stl
import stl.boolean_eval
import stl.fastboolean_eval
import traces
from nose2.tools import params
import unittest
from sympy import Symbol

ex1 = ("2*A > 3", False)
ex2 = ("F[0, 1](2*A > 3)", True)
ex2 = ("F(2*A > 3)", True)
ex2 = ("F[0, inf](2*A > 3)", True)
ex3 = ("F[1, 0](2*A > 3)", False)
ex4 = ("G[1, 0](2*A > 3)", True)
ex5 = ("(A < 0)", False)
ex6 = ("G[0, 0.1](A < 0)", False)
ex7 = ("G[0, 0.1](C)", True)
ex8 = ("G[0, 0.2](C)", False)
ex9 = ("(F[0, 0.2](C)) and (F[0, 1](2*A > 3))", True)
ex10 = ("(A = 1) U (A = 4)", True)
ex11 = ("(A < 5) U (A = 4)", False)
x = {
    "A": traces.TimeSeries([(0, 1), (0.1, 1), (0.2, 4)]),
    "B": traces.TimeSeries([(0, 2), (0.1, 4), (0.2, 2)]),
    "C": traces.TimeSeries([(0, True), (0.1, True), (0.2, False)]),
}

class TestSTLEval(unittest.TestCase):
    @params(ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8, ex9, ex10, ex11)
    def test_eval(self, phi_str, r):
        phi = stl.parse(phi_str)
        stl_eval = stl.boolean_eval.pointwise_sat(phi)
        stl_eval2 = stl.boolean_eval.pointwise_sat(~phi)
        self.assertEqual(stl_eval(x, 0), r)
        self.assertEqual(stl_eval2(x, 0), not r)


"""
    @params(ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8, ex9, ex10, ex11)
    def test_fasteval(self, phi_str, _):
        phi = stl.parse(phi_str)
        stl_eval = stl.boolean_eval.pointwise_sat(phi)
        stl_evalf = stl.fastboolean_eval.pointwise_sat(phi)
        stl_evalf2 = stl.fastboolean_eval.pointwise_sat(~phi)

        b_slow = stl_eval(x, 0)
        b_fast = stl_evalf(x, 0)
        b_fast2 = stl_evalf2(x, 0)
        self.assertEqual(b_slow, b_fast)
        self.assertEqual(b_fast, not b_fast2)
"""
