#!/usr/bin/env python3

"""
This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round.
"""

import random

MOVES = ['rock', 'paper', 'scissors']


class Player:
    """The Player class is the parent class for all Players in this game."""

    def move(self):
        """Return the player's move."""
        return 'rock'

    def learn(self, my_move, their_move):
        """Learn from the player's move and the opponent's move."""
        pass


class RandomPlayer(Player):
    """A player that chooses a random move."""

    def move(self):
        """Return a random move."""
        return random.choice(MOVES)


class HumanPlayer(Player):
    """A human player that chooses a move based on user input."""

    def move(self):
        """Prompt the user for a move and return it."""
        while True:
            user_input = input("Rock, paper, scissors? ").lower()
            if user_input in MOVES:
                return user_input
            print("Invalid input. Please try again.")


class ReflectPlayer(Player):
    """A player that remembers and imitates the opponent's last move."""

    def __init__(self):
        self.their_move = None

    def move(self):
        """Return the opponent's last move, or a random move if not available."""
        return self.their_move or random.choice(MOVES)

    def learn(self, my_move, their_move):
        """Remember the opponent's last move."""
        self.their_move = their_move


class CyclePlayer(Player):
    """A player that cycles through the moves in a specific order."""

    def __init__(self):
        self.my_move = None

    def move(self):
        """Return the next move in the cycle."""
        if self.my_move is None:
            return random.choice(MOVES)
        index = MOVES.index(self.my_move)
        return MOVES[(index + 1) % len(MOVES)]

    def learn(self, my_move, their_move):
        """Remember the player's last move."""
        self.my_move = my_move


def beats(one, two):
    """Return True if move one beats move two, False otherwise."""
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    """A game of Rock, Paper, Scissors."""

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        """Play a single round of the game and return the scores."""
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        if beats(move1, move2):
            print('Player 1 wins the round!')
            p1_score, p2_score = 1, 0
        elif beats(move2, move1):
            print('Player 2 wins the round!')
            p1_score, p2_score = 0, 1
        else:
            print('This round is a tie!')
            p1_score, p2_score = 0, 0

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        return p1_score, p2_score

    def play_game(self):
        """Play a full game and print the final scores and winner."""
        print("Game start!")
        p1_score = p2_score = 0

        for round in range(5):
            print(f"\nRound {round + 1}:")
            round_scores = self.play_round()
            p1_score += round_scores[0]
            p2_score += round_scores[1]

        print(f"\nFinal scores:")
        print(f"Player 1: {p1_score}")
        print(f"Player 2: {p2_score}")

        if p1_score > p2_score:
            print("Player 1 wins the game!")
        elif p2_score > p1_score:
            print("Player 2 wins the game!")
        else:
            print("The game is a tie!")

        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()