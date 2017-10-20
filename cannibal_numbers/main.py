"""Cannibal numbers
Challenge from: https://www.reddit.com/r/dailyprogrammer/comments/76qk58/20171016_challenge_336_easy_cannibal_numbers/
"""
import random

def get_input_int(prompt):
    """Gets the users input once they entered an int"""
    val = None
    while val is None:
        try:
            val = int(input(prompt))
        except ValueError:
            print('Please enter a number')
    return val

def cannibal_numbers(values, query):
    result = 0
    preys_eaten = 0
    values.sort(reverse=True)

    for i_pred, pred in enumerate(values):
        for i_prey, prey in reversed(list(enumerate((values[:-(preys_eaten + 1)])))):
            if i_prey < i_pred:
                return result
            # Check that the prey is not bigger than the query already.
            # Eat it if it's not
            if (prey < query
                and pred < query
                and pred > prey):
                pred += 1
                preys_eaten += 1

            if pred >= query:
                result += 1
                break

    return result

if __name__ == '__main__':
    ####### Get user input #######
    values = [21, 9, 5, 8, 10, 1, 3]
    queries = [10, 15]
    #values = [2, 2, 2, 2]
    #queries = [3]
    #values = [3, 3, 3, 2, 2, 2, 1, 1, 1]
    #queries = [4]
    #values = [1, 2, 3, 4, 5]
    #queries = [5]

    print('Values: {}'.format(values))
    print('Queries: {}'.format(queries))

    ####### Calculate #######
    results = [0 for i in range(len(queries))]

    for q_index, q in enumerate(queries):
        results[q_index] = cannibal_numbers(values, q)

    print(results)