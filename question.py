import numpy as np
import numpy.random as rd
from input_parser import parse

class Question():
    def __init__(self, operation, difficulty=3) -> None:
        self.answered = False  # Q attempted?
        self.correct = False  # Q answered correctly?
        self.op = operation
        self.difficulty = difficulty    

class IntQuestion(Question):
    def __init__(self, operation, difficulty=3) -> None:
        super().__init__(operation, difficulty)
        self.ans_range = 10**difficulty
        self.value_range = 2 * self.ans_range
        self.generate()

    def generate(self):
        self.answer = rd.randint(1, self.ans_range)
        match self.op:
            case '+':
                self.number1 = rd.randint(1, self.value_range - self.answer)
                self.number2 = self.number1 + self.answer
            case '-':
                self.number2 = rd.randint(1, self.value_range - self.answer)
                self.number1 = self.number2 + self.answer
            case '*':
                self.number1 = rd.randint(1, int(self.value_range / self.answer))
                self.number2 = self.number1 * self.answer
            case '/':
                self.number2 =  rd.randint(1, int(self.value_range / self.answer))
                self.number1 = self.number2 * self.answer

    def ask(self):
        self.prompt = '{:d} {} {} = {:d} \n'.format(self.number1, self.op, '???', self.number2)
        print(self.prompt)
        self.user_input = input()
        self.answered = True

    def assess(self):
        value = parse(self.user_input)
        if value == self.answer:
            self.correct = True


class DecQuestion(Question):
    def __init__(self, operation, difficulty=3) -> None:
        super().__init__(operation, difficulty)

        self.mantissa_digits = difficulty
        self.exp_range = (-difficulty+1, difficulty)
        self.generate()

    def generate(self):
        exp = rd.randint(low = self.exp_range[0], high=self.exp_range[1])

        self.answer = rd.random() * 10**exp 
        self.answer = round(self.answer, self.mantissa_digits-exp if exp > 0 else self.mantissa_digits)

        # match self.op:
        #     case '+':
        #         self.number1 = rd.randint(1, self.value_range - self.answer)
        #         self.number2 = self.number1 + self.answer
        #     case '-':
        #         self.number2 = rd.randint(1, self.value_range - self.answer)
        #         self.number1 = self.number2 + self.answer
        #     case '*':
        #         self.number1 = rd.randint(1, int(self.value_range / self.answer))
        #         self.number2 = self.number1 * self.answer
        #     case '/':
        #         self.number2 =  rd.randint(1, int(self.value_range / self.answer))
        #         self.number1 = self.number2 * self.answer

    def ask(self):
        self.prompt = '{:.{}} {} {} = {:.{}} \n'.format(self.number1, self.mantissa_digits, self.op, '???', self.number2, self.mantissa_digits)
        print(self.prompt)
        self.user_input = input()
        self.answered = True

    def assess(self):
        value = parse(self.user_input)
        if value == self.answer:
            self.correct = True


QUESTION_CLASSES = [DecQuestion]
OPERATIONS = ['+', '-', '*', '/']
def generate_questions(N, difficulty=3):
    question_array = np.empty(N, dtype=Question)
    qclasses = rd.choice(QUESTION_CLASSES, N)
    ops = rd.choice(OPERATIONS, N)

    for q in range(N):
        question_array[q] = qclasses[q](ops[q], difficulty)
    return question_array

if __name__ == '__main__':
    qs = generate_questions(10)
    print(qs)
