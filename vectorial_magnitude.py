from sympy import *

import vectorial_function

ELEVATED_TWO = "**2"


def calculate_magnitude(function_f,
                        function_g,
                        function_h,
                        variable):

    function_f = str(simplify(str(function_f)+ "*" + str(function_f)))
    function_g = str(simplify(str(function_g) + "*" + str(function_g)))

    if str(function_h) != "":
        function_h = str(simplify(str(function_h) + "*" + str(function_h)))
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