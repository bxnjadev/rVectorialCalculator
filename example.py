import sympy as sympy
from sympy import *

import vectorial_function

function = vectorial_function.new_function_vector_r2("t**2 + 2", "t-1", "t")

function.derive()
function.derive()

function.show_function()
function.show_function_derivative(1)
function.show_function_derivative(2)

print(
    function.get_magnitude_of_derivative(1)
)