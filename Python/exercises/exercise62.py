from itertools import combinations

vowels = ['A','E','I','O','U']


def count_scores(stuarts_score,kevins_score,length,combinations_list):
    for val in combinations_list:
        print(val[0])
        if val[0] in vowels:
            stuarts_score = stuarts_score + 1
        else:
            kevins_score = kevins_score + 1

    return (stuarts_score,kevins_score)


def minion_game(str):

    stuarts_score = 0
    kevins_score = 0

    # your code goes here
    for len_of_combinations in range(1,len(str)+1):
       (stuarts_score, kevins_score) = count_scores(stuarts_score,
                    kevins_score,
                    len_of_combinations,
                    list(combinations(str, len_of_combinations)))

    return (stuarts_score,kevins_score)


if __name__ == '__main__':
    # s = input()
    (stuarts_score,kevins_score) = minion_game('BANANA')
    print('Final Scores\n')
    print (stuarts_score,kevins_score)
