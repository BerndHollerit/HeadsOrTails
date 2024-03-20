# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import array
import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.


# Randomly returns Heads or Tails
def heads_or_tails():
    options = ['H', 'T']
    return random.choice(options)


def calculate_scores():
    heads_or_tails_array = array.array('u', [' '] * 100)
    alice_score = 0
    bob_score = 0

    # Perform the first coin toss
    heads_or_tails_array[0] = heads_or_tails()

    for i in range(1, 100):
        heads_or_tails_array[i] = heads_or_tails()

        if heads_or_tails_array[i] == 'H' and heads_or_tails_array[i - 1] == 'H':
            alice_score += 1
        elif heads_or_tails_array[i] == 'T' and heads_or_tails_array[i - 1] == 'H':
            bob_score += 1

    # print("Alice Score: {}".format(alice_score))
    # print("Bob Score: {}".format(bob_score))
    return alice_score, bob_score


def run_simulation():
    number_of_simulations = 10000

    alice_scores = array.array('i', [0] * number_of_simulations)
    bob_scores = array.array('i', [0] * number_of_simulations)

    for i in range(number_of_simulations):
        alice_score, bob_score = calculate_scores()
        alice_scores[i] = alice_score
        bob_scores[i] = bob_score

    alice_sum = sum(alice_scores)
    bob_sum = sum(bob_scores)

    expected_value_alice = alice_sum / number_of_simulations
    expected_value_bob = bob_sum / number_of_simulations

    print("Expected Value Alice: {}".format(expected_value_alice))
    print("Expected Value Bob: {}".format(expected_value_bob))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_simulation()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
