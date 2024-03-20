# Flip a fair coin 100 times - it gives a sequence of heads (H) and tails (T). For each HH in the sequence of flips,
# Alice gets a point; for each HT, Bob does, so e.g. for the sequence THHHT Alice gets 2 points and Bob gets 1 point.
# Who is most likely to win?

import array
import random


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

    for i in range(100):
        heads_or_tails_array[i] = heads_or_tails()

        if heads_or_tails_array[i] == 'H' and heads_or_tails_array[i - 1] == 'H':
            alice_score += 1
        elif heads_or_tails_array[i] == 'T' and heads_or_tails_array[i - 1] == 'H':
            bob_score += 1

    return alice_score, bob_score


def run_simulation():
    number_of_simulations = 100000
    alice_wins = 0
    bob_wins = 0
    draws = 0

    for i in range(number_of_simulations):
        alice_score, bob_score = calculate_scores()
        if alice_score > bob_score:
            alice_wins += 1
        elif bob_score > alice_score:
            bob_wins += 1
        else:
            draws += 1

    print(f"Simulations: {number_of_simulations}")
    print(f"Alice Wins :  {alice_wins}")
    print(f"Bob Wins   :  {bob_wins}")
    print(f"Draws      :   {draws}")


if __name__ == '__main__':
    run_simulation()
