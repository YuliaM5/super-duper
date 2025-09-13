from sympy import symbols, diff, simplify, pprint
from sympy.parsing.sympy_parser import parse_expr

def calculate(func):
    return simplify(diff(parse_expr(func), symbols('x'), 1))



f = "E**(x**2)"

pprint(calculate(f))