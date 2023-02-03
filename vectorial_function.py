from sympy import *

import unitary_vector
import vectorial_magnitude

WITHOUT_DIMENSION = "without_dimension"
R_2 = "R_2"
R_3 = "R_3"


class VectorialFunction:
    derives = []
    tangent_vector = []

    def __init__(self,
                 function_f,
                 function_g,
                 function_h,
                 variable):
        self.function_f = function_f
        self.function_g = function_g
        self.function_h = function_h

        if self.function_h == "":
            self.function_h = WITHOUT_DIMENSION

        self.variable = variable

    def show_general_function(self, prefix, function_f, function_g, function_h):

        if self.get_dimension() == R_2:
            print(prefix + " = {f}i + {g}j".format(
                f=function_f,
                g=function_g,
            ))
            return

        print(prefix + " = {f}i + {g}j + {h}k".format(
            f=function_f,
            g=function_g,
            h=function_h
        ))

    def show_function(self):
        self.show_general_function("r(t)", self.function_f, self.function_g, self.function_h)

    def show_function_derivative(self, order):
        derivative = self.get_derivative(order)

        derivative_symbol = "'" * order
        prefix = "r(t)" + derivative_symbol

        self.show_general_function(prefix, derivative[0], derivative[1], derivative[2])

    def show_unitary_tangent_vector(self):

        if len(self.tangent_vector) == 0:
            self.calculate_tangent_vector()

        self.show_general_function("T(t)", self.tangent_vector[0],
                                   self.tangent_vector[1],
                                   self.tangent_vector[2])

    def get_derivative(self, order):
        order = order - 1

        if order < 0:
            return self.get_derivative(1)

        return self.derives[order]

    def calculate_tangent_vector(self):
        self.tangent_vector = unitary_vector.calculate_tangent_vector(self)
    def get_dimension(self):
        if self.function_h == WITHOUT_DIMENSION:
            return R_2
        return R_3

    def get_derivative_in_top(self):
        derive = []

        if len(self.derives) == 0:
            derive.append(self.function_f)
            derive.append(self.function_g)

            if self.get_dimension() == R_3:
                derive.append(self.function_h)

            return derive

        return self.derives[len(self.derives) - 1]

    def derive(self):
        derive = []

        derivative_top = self.get_derivative_in_top()

        function_f_derivative = diff(derivative_top[0], self.variable)
        function_g_derivative = diff(derivative_top[1], self.variable)

        derive.append(
            function_f_derivative
        )
        derive.append(
            function_g_derivative
        )

        if self.get_dimension() == R_3:
            function_h_derivative = diff(derivative_top[2], self.variable)
            derive.append(
                function_h_derivative
            )

        self.derives.append(derive)

    def get_magnitude(self):
        return vectorial_magnitude.calculate_magnitude(
            self.function_f, self.function_g, self.function_h
        )

    def get_magnitude_of_derivative(self, order):
        derivative = self.get_derivative(order)

        function_h = ""

        if self.get_dimension() == R_3:
            function_h = derivative[2]

        return vectorial_magnitude.calculate_magnitude(
            derivative[0], derivative[1], function_h
        )


def new_function_vector_r3(function_f, function_g, function_h, variable):
    return VectorialFunction(function_f, function_g, function_h, variable)


def new_function_vector_r2(function_f, function_g, variable):
    return VectorialFunction(function_f, function_g, WITHOUT_DIMENSION, variable)
