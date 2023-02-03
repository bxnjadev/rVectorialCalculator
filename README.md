# rVectorialCalculator


rVectorialcalculator is a calculator for vectorial calculus, with she, we calculate the first, second or n derivative of a vectorial function.

# Use

The project handle a class for the vectorials functions, VectorialFunction class.

For create a vectorial function:

```
function = vectorial_function.new_function_vector_r3("sin(t)", "cos(t)", "t", "t")
```

I'ts possible create functions in r2 or r3.

The VectorialFunction class has a method for derive.

```
function.derive()
```

Every time the function is called, this will calculate the derivative major.

And for show the function derivative.

```
function.show_function_derivative(order)
```

#Example

```
function = vectorial_function.new_function_vector_r3("sin(t)", "cos(t)", "t", "t")

function.derive()
function.derive()

function.show_function()
function.show_function_derivative(1)
function.show_function_derivative(2)
```

Console showed:
```
r(t) = sin(t)i + cos(t)j + tk
r(t)' = cos(t)i + -sin(t)j + 1k
r(t)'' = -sin(t)i + -cos(t)j + 0k
```

Where order is the order of derivative.

This project usted sympy, https://www.sympy.org/es/
