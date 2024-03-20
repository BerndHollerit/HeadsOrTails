# Flip a fair coin 100 times - it gives a sequence of heads (H) and tails (T). For each HH in the sequence of flips,
# Alice gets a point; for each HT, Bob does, so e.g. for the sequence THHHT Alice gets 2 points and Bob gets 1 point.
# Who is most likely to win?

import array
import random


# Randomly returns Heads (H) or Tails (T)
def heads_or_tails():
    options = ['H', 'T']
    return random.choice(options)


def calculate_points():
    coin_toss_sequence = array.array('u', [' '] * 100)
    alice_points = 0
    bob_points = 0

    # Perform the first coin toss. This one does not need a check for the sequence
    coin_toss_sequence[0] = heads_or_tails()

    for i in range(1, 100):
        coin_toss_sequence[i] = heads_or_tails()

        if coin_toss_sequence[i] == 'H' and coin_toss_sequence[i - 1] == 'H':
            alice_points += 1
        elif coin_toss_sequence[i] == 'T' and coin_toss_sequence[i - 1] == 'H':
            bob_points += 1

    return alice_points, bob_points


def run_simulation():
    number_of_simulations = 100000
    alice_wins = 0
    bob_wins = 0
    draws = 0

    for i in range(number_of_simulations):
        alice_points, bob_points = calculate_points()
        if alice_points > bob_points:
            alice_wins += 1
        elif bob_points > alice_points:
            bob_wins += 1
        else:
            draws += 1

    print(f"Simulations: {number_of_simulations}")
    print(f"Alice Wins :  {alice_wins}")
    print(f"Bob Wins   :  {bob_wins}")
    print(f"Draws      :   {draws}")


if __name__ == '__main__':
    run_simulation()
