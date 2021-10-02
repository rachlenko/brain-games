#!/usr/bin/env python
import sys
import games.progression as progression
import games.summarize as summarize
import games.divide as divide
import games.multiply as multiply


def main():
    wellcome_msg()

    game_id = sys.stdin.readline()
    log("game_id is {}".format(game_id.strip()))

    if int(game_id.strip()) not in range(5):
        log("wrong number has been choose {}".format(game_id))
        end_game()
    username = get_username()
    run_game(game_id, username)


def run_game(game_id, username):
    if int(game_id) == 1:
        correct_answers, missed_answers = progression.run(username)
        end_game(username, correct_answers, missed_answers)
    if int(game_id) == 2:
        summarize.run()
    if int(game_id) == 3:
        divide.run()
    if int(game_id) == 4:
        multiply.run()
    if int(game_id) == 0:
        end_game()


def get_username():
    print("May I have your name?")
    username = sys.stdin.readline().strip()
    print(f"Hello, {username}!")
    return username


def log(msg, debug=0):
    if debug:
        print(msg)


def end_game(username, correct_answers, missed_answers):
    """
    save users score
    print out goodbye message
    """
    print(
        f"""You score is :
        {correct_answers} correct answers
        {missed_answers} missed answers"""
    )
    log(
        f"""updated score in db:
            correct answers {correct_answers}
            missed answers {missed_answers}
           """
    )
    # TODO here should be question : "do you like to continue? "
    print(f"Goodbye {username}!")


def wellcome_msg():
    print("Welcome to the Brain Game!")
    print()
    print()
    print()
    print(
        """choose your game :
        [1] progression
        [2] summarize
        [3] divide
        [4] multiply
        [0] exit
        """
    )


if __name__ == "__main__":
    main()
