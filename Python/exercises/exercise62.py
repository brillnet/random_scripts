from itertools import combinations

vowels = ['a','e','i','o','u']

def count_scores(length,combinations_list):
    print('Length is: ' + str(length))
    for val in combinations_list:
        if val[0] == in vowels:

def minion_game(str):

    stuart = 0
    kevin = 0

    # your code goes here
    for len_of_combinations in range(1,len(str)+1):
        count_scores(len_of_combinations,list(combinations(str, len_of_combinations)))


if __name__ == '__main__':
    # s = input()
    minion_game('BANANA')