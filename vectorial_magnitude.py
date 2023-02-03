from sympy import *

import vectorial_function

ELEVATED_TWO = "**2"


def calculate_magnitude(function_f,
                        function_g,
                        function_h,
                        variable):

    function_f = str(simplify(function_f ** 2))
    function_g = str(simplify(function_g ** 2))

    if str(function_h) != "":
        function_h = str(simplify(function_h ** 2))
    else:
        return sqrt(
            simplify(
                function_f + " + " + function_g
            ))

    return sqrt(
        simplify(
            function_f + " + " + function_g + " + " + function_h
        )
    )