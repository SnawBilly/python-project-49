#!/usr/bin/env python3


from math import gcd
from random import randint
import prompt


def gcd_():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    if name:
        print(f'Hello, {name}')
        print('Find the greatest common divisor of given numbers.')
        count = 0
        for _ in range(3):
            num1 = randint(1, 100)
            num2 = randint(1, 100)
            divisor = gcd(num1, num2)
            print(f"Question: {num1} {num2}")
            n = prompt.integer('Your Answer: ')
            if n == divisor:
                print('Correct!')
                count += 1
            else:
                print(f"'{n}' is wrong answer ;(. Correct answer was '{divisor}'.\nLet's try again, {name}!")
                break
    if count == 3:
        print(f'Congratulations, {name}!')
def main():
    gcd_()
if __name__ == '__main__':
    main()
