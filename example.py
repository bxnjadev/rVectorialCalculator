import sympy as sympy
from sympy import *

import vectorial_function

function = vectorial_function.new_function_vector_r3("sin(t)", "cos(t)", "t", "t")

function.derive()

function.show_unitary_tangent_vector()
