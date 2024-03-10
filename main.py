import time
import numpy as np
import numpy.random as rd
import math
from fractions import Fraction
from decimal import Decimal
from question import generate_questions

# actual values
TIME_LIMIT = 8 * 60
N_QUESTIONS = 80

# testing values
# TIME_LIMIT = 10 # s
# N_QUESTIONS = 5

questions = generate_questions(N_QUESTIONS)

runtime = 0.0
starttime = time.time()
for n_question in range(N_QUESTIONS):
    runtime = time.time() - starttime
    if runtime > TIME_LIMIT:
        print('time\'s up!')
        break
    elif n_question >= N_QUESTIONS-1:
        print('all questions answered!')
        break
    else:
        q = questions[n_question]
        print('Question {} out of {}'.format(n_question+1, N_QUESTIONS))
        q.ask()
        q.assess()

sum_answered  = sum([
        int(q.answered) for q in questions
    ])

sum_correct = sum([
        int(q.correct and q.answered) for q in questions
    ])

sum_incorrect = int(sum_answered  - sum_correct)
sum_unanswered = int(N_QUESTIONS - sum_answered)

score = sum_correct - 2 * sum_incorrect  # arbitrary score metric

print('you answered {:d} questions out of {:d}'.format(sum_answered, N_QUESTIONS))
print('you answered {:d} questions correctly and {:d} incorrectly'.format(sum_correct, sum_incorrect))
print('your score is: {:d}'.format(score))

# store results

