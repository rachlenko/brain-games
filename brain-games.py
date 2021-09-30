#!/usr/bin/env python
import sys
import games.progression as progression
import games.summarize as summarize
import games.divide as divide
import games.multiply as multiply


def main():
    print("welcome to brain game")
    print("enter your name:")
    username = sys.stdin.readline()
    print_bunner()
    print("hello {}".format(username))

    print(
        """choose your game :
        [1] progression
        [2] summarize
        [3] divide
        [4] multiply
        [0] exit
        """
    )

    game_id = sys.stdin.readline()
    log("game_id is {}".format(game_id.strip()))

    if int(game_id.strip()) not in range(5):
        log("wrong number has been choose {}".format(game_id))
        end_game(username)
    run_game(game_id)
    progression.run()


def run_game(game_id):
    if int(game_id) == 1:
        progression.run()
    if int(game_id) == 2:
        summarize.run()
    if int(game_id) == 3:
        divide.run()
    if int(game_id) == 4:
        multiply.run()
    if int(game_id) == 0:
        end_game()


def log(msg):
    print(msg)


def end_game(username):
    """
    save users score
    print out goodbye message
    """
    print("goodbye {}".format(username))


def print_bunner():
    print()
    print()
    print()


if __name__ == "__main__":
    main()
