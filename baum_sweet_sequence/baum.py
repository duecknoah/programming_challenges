"""
[2017-12-11] Challenge #344 [Easy] Baum-Sweet Sequence

Link:
https://www.reddit.com/r/dailyprogrammer/comments/7j33iv/20171211_challenge_344_easy_baumsweet_sequence/
"""

def get_baum(number):
    """
    In mathematics, the Baum–Sweet sequence is an infinite automatic
    sequence of 0s and 1s defined by the rule:
        b_n = 1 if the binary representation
            of n contains no block of
            consecutive 0s of odd length;
        b_n = 0 otherwise;
    """

    # Create binary sequence
    num_bits = len(bin(number)) - 2
    bits = [(number >> bit) & 1 for bit in range(num_bits - 1, -1, -1)]
    seq_len = 0

    if number == 0:
        return 1

    # Loop through, if a sequence of 0's is of odd length, return 0
    for idx, i in enumerate(bits):
        if i == 0:
            seq_len += 1

        if i == 1 or idx + 1 == num_bits:
            # end of sequence, check If odd length of 0's block
            if seq_len % 2 == 1:
                return 0
            # Else reset
            seq_len = 0

    # No odd blocks detected
    return 1

if __name__ == '__main__':
    try:
        n = int(input('Set \'n\' where \'n\' is the last number of the sequence 0-\'n\': '))
        print([get_baum(i) for i in list(range(n + 1))])
    except ValueError:
        print('Value entered is not a number')