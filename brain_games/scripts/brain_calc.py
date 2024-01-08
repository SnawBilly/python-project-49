#!/usr/bin/env python3


from random import randint, choice
import prompt


def calc():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    if name:
        print(f'Hello, {name}')
        print('What is the result of the expression?')
        count = 0
        for _ in range(3):
            num1 = randint(1, 30)
            num2 = randint(1, 30)
            operator = choice('+-*')
            if operator == '+':
                action = num1 + num2
            elif operator == '-':
                action = num1 - num2
            elif operator == '*':
                action = num1 * num2
            print(f"Question: {num1} {operator} {num2}")
            n = prompt.integer('Your Answer: ')
            if n == action:
                print('Correct!')
                count += 1
            else:
                print(f"'{n}' is wrong answer ;(. Correct answer was '{action}'.\nLet's try again, {name}!")
                break
    if count == 3:
        print(f'Congratulations, {name}!')


def main():
    calc()
if __name__ == '__main__':
    main()
