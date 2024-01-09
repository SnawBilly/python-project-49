#!/usr/bin/env python3


from random import randint, choice
import prompt


def prime():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    for _ in range(3):
        answer_count = 1
        num = randint(1, 100)
        for i in range(1, num // 2 + 1):
            if num % i == 0:
                answer_count += 1
        if answer_count == 2:
            answer = 'yes'
        else:
            answer = 'no'
        print(f"Question: {num}")
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
    prime()


if __name__ == '__main__':
    main()
