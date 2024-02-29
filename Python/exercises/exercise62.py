

vowels = ['A','E','I','O','U']


# def count_scores(stuarts_score,kevins_score):

#     for val in combinations_list:
#         print(val[0])
#         if val[0] in vowels:
#             stuarts_score = stuarts_score + 1
#         else:
#             kevins_score = kevins_score + 1

#     return (stuarts_score,kevins_score)


def minion_game(str):

    stuarts_score = 0
    kevins_score = 0
    substrings = {}

    #  First pass
    #  B,A,N,A,N,A
    #  Second pass
    #  BA,AN,NA,AN,NA
    #  Third pass
    #  BAN,ANA,NAN,ANA
    #  Fourth pass
    #  BANA,ANAN,NANA,

    #  Increase slice size by 1 on each pass.


    substring_length = 1

    for index in range(0,len(str)):

        print('Substring length: ' + str(substring_length))
        if substring_length == 1:
            print(str[index])
        else:



        #  second pass
        [0,1] [1,2],[2,3],[3,4],[4,5]
        print(str[index])

        #  third pass
        [0,2], [1,3], [2,4], [3,5]

        #  fourth pass
        [0,3], [1,4], [2,5]

    # your code goes here



if __name__ == '__main__':
    # s = input()
    minion_game('BANANA')
    print('Final Scores\n')
    print (stuarts_score,kevins_score)
