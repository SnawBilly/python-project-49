#!/usr/bin/env python3


from random import randint, choice
import prompt


def progression():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    if name:
        print(f'Hello, {name}')
        print('What number is missing in the progression?')
        count = 0
        for _ in range(3):
            num_progress = randint(1, 10)
            first_num = randint(1, 100)
            lst = [first_num]
            for _ in range(9):
                first_num += num_progress
                lst.append(first_num)
            random_num = randint(0, 9)
            answer = lst[random_num]
            lst[random_num] = '..'
            print("Question: ", end = '')
            print(*lst)
            n = prompt.integer('Your Answer: ')
            if n == answer:
                print('Correct!')
                count += 1
            else:
                print(f"'{n}' is wrong answer ;(. Correct answer was '{answer}'.\nLet's try again, {name}!")
                break
    if count == 3:
        print(f'Congratulations, {name}!')


def main():
    progression()


if __name__ == '__main__':
    main()
