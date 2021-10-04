#!/usr/bin/env python

import random
import sys


def run(username):
    print("What number is missing in this progression?")
    # initialization
    questions_round = 3
    correct_answers = 0
    round_number = 0

    # rounds loop
    while round_number < questions_round:

        count_decor = 0
        str_progression = ""
        for i in gen_progression():
            if count_decor == 2:
                str_progression = f"{str_progression} .. "
                generated_answer = i
            else:
                str_progression = f"{str_progression} {i} "
            count_decor += 1
        print(f"Question: {str_progression}")

        user_answer = sys.stdin.readline().strip()
        print(f"your answer is {user_answer}")

        if check_answer(user_answer, generated_answer, username):
            correct_answers += 1

        round_number += 1

    return summary(correct_answers, questions_round, username)


def gen_progression():
    step = random.randrange(1, 15)
    start_number = random.randrange(90, 250)

    tmp_array = []
    for i in range(0, start_number, step):
        tmp_array.append(i)

    return tmp_array[-8:]


def check_answer(user_answer, generated_answer, username):

    if int(generated_answer) == int(user_answer):
        print("Correct!")
        return True
    else:
        print(
            f""" '{user_answer}' is wrong answer;
                Correct answer was {generated_answer}. """
        )
        print(f"Let's try again, {username}!")
        return False


def summary(correct_answers, questions_round, username):
    missed_answers = 0
    if correct_answers == questions_round:
        print(f"Congratulations, {username}!")
    else:
        missed_answers = questions_round - correct_answers
        print("\n\nGame over")
    return (correct_answers, missed_answers)


if "__main__" == __name__:
    run()
