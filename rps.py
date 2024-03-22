#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random

MOVES = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def __init__(self):
        self.my_move = None
        self.their_move = None

    def move(self):
        return random.choice(MOVES)


class HumanPlayer(Player):
    def __init__(self):
        self.my_move = None
        self.their_move = None

    def move(self):
        while True:
            user_input = input("Rock, paper, scissors? ").lower()
            if user_input in MOVES:
                return user_input.lower()
            else:
                print("Invalid input. Please try again.")


class ReflectPlayer(Player):
    def __init__(self):
        self.their_move = None

    def move(self):
        if self.their_move is None:
            return_move = random.choice(MOVES)
        else:
            return_move = self.their_move
        return return_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.my_move = None

    def move(self):
        if self.my_move is None:
            return random.choice(MOVES)
        elif self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        else:
            return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1score = 0
        self.p2score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if move1 != move2:
            result = beats(move1, move2)
            if result:
                print('Player 1 won round')
                self.p1score += 1
            else:
                print('Player 2 won round')
                self.p2score += 1
        else:
            print('Tie round')
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for game_round in range(5):
            print(f"\nRound {game_round + 1}:")
            self.play_round()
        print(f"\nPlayer 1 score: {self.p1score}")
        print(f"Player 2 score: {self.p2score}")
        print("-" * 20)
        if self.p1score > self.p2score:
            print("Player 1 wins game!")
        elif self.p2score > self.p1score:
            print("Player 2 wins game!")
        else:
            print("It's a tie!")
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
