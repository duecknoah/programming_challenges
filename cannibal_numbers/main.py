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

    # Remove numbers already meeting the query number
    for v in values:
        if v >= query:
            values.remove(v)
            result += 1

    values.sort(reverse=True)

    for i_pred in range(len(values)):

        pred = values[i_pred]

        # Don't count None values
        if pred is None:
            continue

        for i_prey in reversed(range(len(values))):

            # Don't count None values
            if values[i_prey] is None:
                continue

            # Don't compare with self
            if (pred == values[i_prey]):
                continue

            # If predator can eat prey
            if pred > values[i_prey]:
                pred += 1
                values[i_prey] = None
                if (pred == query):
                    result += 1
                    break


    '''
    for i_pred, pred in enumerate(values):
        for i_prey, prey in reversed(list(enumerate((values[:-(preys_eaten + 1)])))):
            if (prey < query
                and pred < query
                and pred > prey):
                print('{} consumed {}'.format(pred, prey))
                pred += 1
                preys_eaten += 1
                print(values)

            if pred >= query:
                result += 1
                break
    '''

    return result

def cannibal_get_results_for(values, queries, expected_result):
    results = []
    for q in queries:
        results.append(cannibal_numbers(values.copy(), q))
    print('Values: {} | Queries: {} | Expected Result: {} | Result: {}'.format(
        values, queries, expected_result, results
    ))
    if results != expected_result:
        raise BaseException("Wrong result for the above answer")

if __name__ == '__main__':

    cannibal_get_results_for([21, 9, 5, 8, 10, 1, 3], [10, 15], [4, 2])
    cannibal_get_results_for([2, 2, 2, 2], [3], [0])
    cannibal_get_results_for([1, 2, 3, 4], [5], [2])
    cannibal_get_results_for([3, 3, 3, 2, 2, 2, 1, 1, 1], [4], [4])


    print("Success!")