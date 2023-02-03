from sympy import *

import vectorial_magnitude

WITHOUT_DIMENSION = "without_dimension"
R_2 = "R_2"
R_3 = "R_3"


class VectorialFunction:
    derives = []

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

    def show_function(self):

        if self.get_dimension() == R_2:
            print("r(t) = {f}i + {g}j".format(
                f=self.function_f,
                g=self.function_g,
            ))
            return

        print("r(t) = {f}i + {g}j + {h}k".format(
            f=self.function_f,
            g=self.function_g,
            h=self.function_h
        ))

    def show_function_derivative(self, order):
        derivative = self.get_derivatives(order)

        derivative_symbol = "'" * order

        if self.get_dimension() == R_2:
            print("r(t)" + derivative_symbol + " = {f}i + {g}j".format(
                f=derivative[0],
                g=derivative[1],
            ))
            return

        print("r(t)" + derivative_symbol + " = {f}i + {g}j + {h}k".format(
            f=derivative[0],
            g=derivative[1],
            h=derivative[2]
        ))

    def get_derivatives(self, order):
        order = order - 1

        if order < 0:
            return self.get_derivatives(1)

        return self.derives[order]

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
            self.function_f, self.function_g, self.function_h, self.variable
        )

    def get_magnitude_of_derivative(self, order):
        derivative = self.get_derivatives(order)

        return vectorial_magnitude.calculate_magnitude(
            derivative[0], derivative[1], derivative[2], self.variable
        )


def new_function_vector_r3(function_f, function_g, function_h, variable):
    return VectorialFunction(function_f, function_g, function_h, variable)


def new_function_vector_r2(function_f, function_g, variable):
    return VectorialFunction(function_f, function_g, WITHOUT_DIMENSION, variable)

