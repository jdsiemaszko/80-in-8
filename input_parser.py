from fractions import Fraction
from decimal import Decimal

def parse(input):  
    if not input:
        print('empty input detected! \n')
        return -1
    if any(char.isalpha() for char in input):
        print('letters detected in input! \n')
        return -1
    elif '-' in input:
        print('negative values detected in input! \n')
        return -1
    elif '/' in input:
        value = Fraction(input.split('/'))
    elif '.' in input:
        value = float(input)
    else:
        value = int(input)

    return value