from math import sin, pi, cos
import random

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    exprs = []


    expr = lambda x, y: (x * 2) - 1
    exprs.append(expr)
    expr = lambda x,y: sin(pi * sin(pi * sin(pi *
             (sin(pi * sin(pi * sin(pi *
             sin(pi * cos(pi * y))))) * cos(pi * sin(
              pi * cos(pi)))))))
    exprs.append(expr)
    expr = lambda x, y: x**2 + y**3
    exprs.append(expr)
    expr = lambda x, y: y**x
    exprs.append(expr)
    expr = lambda x, y: (x**3+8)/(x**3+x**2-x-12)
    exprs.append(expr)
    expr = lambda x, y: sin(x*y**4)*cos(3*x)
    exprs.append(expr)
    expr = lambda x, y: sin(x + y**2 - 3*x)
    exprs.append(expr)
    expr = lambda x, y: sin(x+pi/4)-cos(x+pi/4)
    exprs.append(expr)
    expr = lambda x, y: sin(x*y) + sin(x)*cos(3*x)
    exprs.append(expr)
    # expr = lambda x, y: sin(x-1.1)/(x-1.1)
    # exprs.append(expr)
    expr = lambda x, y: abs(sin(x)**cos(3*x))
    exprs.append(expr)
    expr = lambda x, y: (sin(pi*x) * cos(pi*x*y) * sin(pi*y))
    exprs.append(expr)
    expr = lambda x, y: sin(pi*x*cos(pi*x*y*sin(pi *(cos(pi*x*y)))))
    exprs.append(expr)
    expr = lambda x, y: 1 - 2 / (1 + x*x) ** 8
    exprs.append(expr)
    expr = lambda x, y: 1 - 2 * abs(x)
    exprs.append(expr)


    #print('random.seed() is {}'.format(random.seed()))
    return random.choice(exprs)
    #return expr

def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr(x, y)
