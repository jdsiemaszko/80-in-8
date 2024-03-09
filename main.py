import time
import numpy as np
import numpy.random as rd
from ops import add, sub, mul, div
import math
from fractions import Fraction
from decimal import Decimal
# actual values
# TIME_LIMIT = 8 * 60
# N_QUESTIONS = 80

# testing values
TIME_LIMIT = 10 # s
N_QUESTIONS = 5

# question type definitions
operations = np.array(['+', '-', '*', '/'])
funcs = {key:value for (key, value) in zip(operations, [add, sub, mul, div])}
syntaxes = np.array(['int', 'dec', 'frac'])  # missing int_frac implementation

# generate arrays
correct = []

# generate question types (should probably generate all questions in advance)
op_array = rd.choice(operations, N_QUESTIONS)
sx_array = rd.choice(syntaxes, N_QUESTIONS)

runtime = 0.0
starttime = time.time()
for n_question in range(N_QUESTIONS):
    op = op_array[n_question]
    sx = sx_array[n_question]

    match sx:
        case 'int':
            answer = rd.randint(0, 1000)
            number1 = rd.randint(0, 1400)
            number2 = funcs[op](number1, answer)

        case 'dec':
            exp = rd.randint(-3, 2)
            mantissa = rd.randint(0, int(10**min(exp+4, 3))) # max three decimal places
            answer = mantissa * 10 ** exp

            exp2 = rd.randint(-3, 2)
            mantissa2 = rd.randint(0, int(10**min(exp+4, 3))) # max three decimal places

            number1 = mantissa2 * 10 ** exp2

            number2 = funcs[op](number1, answer)
            
        case 'frac':
            num = rd.randint(0, 100, dtype=int)
            den = rd.randint(0, 100, dtype=int)
            answer = Fraction(num, den)

            num2 = rd.randint(0, 100, dtype=int)
            den2 = rd.randint(0, 100, dtype=int)
            number1 = Fraction(num2, den2)

            number2 = funcs[op](number1, answer)


        case 'int_frac':
            answer = rd.randint(0, 1000)
            number1 = rd.randint(0, 2000)
            number2 = funcs[op](number1, answer)

    runtime = time.time() - starttime
    if runtime > TIME_LIMIT:
        print('time\'s up!')
        break
    elif n_question >= N_QUESTIONS-1:
        print('all questions answered!')
        break
    else:
        print('Question {} out of {}'.format(n_question+1, N_QUESTIONS))
        match sx:
            case 'int':
                prompt = '{} {} {} = {} \n'.format(number1, op, '???', number2)
                inp = input()
            case 'frac':
                prompt = '{}/{} {} {} = {}/{} \n'.format(number1.numerator,
                                                           number1.denominator,
                                                             op, '???', number2.numerator,
                                                               number2.denominator)
            case 'dec':
                prompt = '{:.3f} {} {} = {:.3f} \n'.format(number1, op, '???', number2)
        print(prompt)
        inp = input()
        
        if input_parser(inp):  # implement parser
            correct.append(True)
        else:
            correct.append(False)

sum_correct = int(sum(correct))
sum_answered  = int(len(correct))
sum_incorrect = int(sum_answered  - sum_correct)
sum_unanswered = int(N_QUESTIONS - sum_answered)
score = sum_correct - 2 * sum_incorrect
print('you answered {:d} questions out of {:d}'.format(sum_answered, N_QUESTIONS))
print('you answered {:d} questions correctly and {:d} incorrectly'.format(sum_correct, sum_incorrect))
print('your score is: {:d}'.format(score))

# store results

