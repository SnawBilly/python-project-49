#!/usr/bin/env python3


from random import randint
import prompt


def even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    if name:
        print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    for _ in range(3):
        num = randint(1, 100)
        answer = ''
        if num % 2 == 0:
            answer = 'yes'
        else:
            answer = 'no'
        print(f'Question: {num}')

        n = prompt.string('Your Answer: ')

        if n == answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{n}' is wrong answer ;(. Correct answer was '{answer}'.\nLet's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')


def main():
    even()


if __name__ == '__main__':
    main()
