import sympy as sympy
from sympy import *

import vectorial_function

function = vectorial_function.new_function_vector_r3("sin(t)", "cos(t)", "t", "t")

function.derive()
function.derive()

print(
    function.get_magnitude()
)

print(
    function.get_magnitude_of_derivative(1)
)