import math


def multiplication(a, b):
    return n(split_operation(a)) * n(split_operation(b))


def divide(a, b):
    return n(split_operation(a)) / n(split_operation(b))


def summarize(a, b):
    return n(split_operation(a)) + n(split_operation(b))


def subtraction(a, b):
    return n(split_operation(a)) - n(split_operation(b))


def power_of(a, b):
    return n(split_operation(a)) ** n(split_operation(b))


def root_of(a, b):
    b = n(split_operation(b))
    for _ in range(n(split_operation(a))):
         b = b ** 0.5
    return b


def logarithmus(a):
    return math.log(n(split_operation(a)))


def re_multiplication(a, b, e):
    return f'{e}/{a}' if b == 'x' else f'{e}/{b}'


def re_divide(a, b, e):
    return f'{a}/{e}' if b == 'x' else f'{e}*{b}'


def re_summarize(a, b, e):
    return f'{e}-{a}' if b == 'x' else f'{e}-{b}'


def re_subtraction(a, b, e):
    return f'{a}-{e}' if b == 'x' else f'{e}+{b}'


def re_power_of(a, b, e):
    if a == 'x':
        i = 0
        for char in b:
            if char in ('+-*/^|'):
                op = b[i]
                rest = b[i+1:]
                e = revert_operation[op]('x', rest, e)
            i += 1
    if b == 'x':
        i = -1
        for char in a[::-1]:
            if char in ('+-*/^|'):
                op = b[i]
                rest = b[0:i]
                e = revert_operation[op](rest, 'x', e)
            i -= 1
    return f'{a}|({e})' if b == 'x' else f'l({e})/l({b}'


stored_vars = {}

# after splitting down the equation string to a operation return value as numerical


def n(x):
    print(x)
    try:
        if type(x) == str:
            if '.' in x:
                return float(x)
            else:
                return int(x)
        else:
            return x
    except:
        return x

# dict of operation char linking to its function


math_operator = {'+': summarize, '-': subtraction, '*': multiplication, '/': divide, '^': power_of, '|': root_of}

revert_operation = {'+': re_summarize, '-': re_subtraction, '*': re_multiplication, '/': re_divide, '^': power_of, '|': root_of}


# needed for make * / operations get handled first


operation_order = (('+', '-'), ('*', '/', '^', '|'))


def split_operation(string):
    for key, foo in math_operator.items():
        if key in string:
            subs = string.split(key)
            return foo(subs[0].strip(), subs[1].strip())
    return string


def var_handle(equation):
    key_list = sorted(list(stored_vars.keys()), key=len, reverse=True)
    new_var = False
    if '=' in equation:
        strings = equation.split('=')
        if strings[0].startswith('$'):
            new_var = strings[0].replace('$', '').strip()
            equation = strings[1]
        elif strings[1].replace('$', ''):
            new_var = strings[1].replace('$', '').strip()
            equation = strings[0]
    if new_var is not False:
        if new_var in key_list:
            key_list.remove(new_var)
    for key in key_list:
        if key in equation:
            equation = equation.replace(key, str(stored_vars[key]))
    print(equation, stored_vars)
    return new_var, equation


def closure_handle(equation, closure=('(', ')')):
    equation = equation.replace('()', '')
    if closure[0] in equation:
        depth = 0
        string = ''
        for char in equation:
            if char == closure[0]:
                depth += 1
            elif char == closure[1]:
                return closure_handle(string)
            if depth > 0:
                string += char
    else:
        return equation


def split_equation_for_x(equation):
    pos_x = equation.index('x')
    print(pos_x, len(equation))
    print(equation)
    if pos_x == 0:
        return [(equation[pos_x], equation[pos_x + 1], equation[pos_x + 2:]), ]
    elif pos_x == len(equation) - 1:
        return [(equation[0:pos_x-1], equation[pos_x-1], equation[pos_x]), ]
    else:
        return [(equation[pos_x], equation[pos_x + 1], equation[pos_x + 2:]),
                (equation[0:pos_x-1], equation[pos_x-1], equation[pos_x])]


def solve_for_x(equation):
    if '=' in equation and 'x' in equation:
        if 'x' in equation.split('=')[1]:
            equal = equation.split('=')[0]
            equation_parts = split_equation_for_x(equation.split('=')[1])
        else:
            equal = equation.split('=')[1]
            equation_parts = split_equation_for_x(equation.split('=')[0])
        for part in equation_parts:
            equal = revert_operation[part[1]](part[0], part[2], equal)
        return equal
    else:
        return False


def calculate(equation):
    if solve_for_x(equation):
        equation = solve_for_x(equation)
    new_var, equation = var_handle(equation)

    if new_var is not False:
        stored_vars[new_var] = str(split_operation(equation))
        print(new_var, '=', equation, '=', stored_vars[new_var])
    else:
        print(equation, '=', split_operation(equation))


if __name__ == '__main__':
    while True:
        print('enter a math equation')
        equation = input('=')
        calculate(equation)
