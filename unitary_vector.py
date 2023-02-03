from sympy import *


def calculate_tangent_vector(vectorial_function):
    magnitude_first_derivative = vectorial_function. \
        get_magnitude_of_derivative(1)

    first_derivative = vectorial_function.get_derivative(1)

    f_component = simplify(first_derivative[0] / magnitude_first_derivative)
    g_component = simplify(first_derivative[1] / magnitude_first_derivative)
    h_component = simplify(first_derivative[2] / magnitude_first_derivative)

    print("h component: ", h_component)

    return [f_component, g_component, h_component]
