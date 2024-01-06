#!/usr/bin/env python3
import prompt
from brain_games.cli import welcome_user
def welcome():
    print('Welcome to the Brain Games!')
    welcome_user()
def main():
    welcome()
if __name__ == '__main__':     
    main()
