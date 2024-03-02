vowels = ['A','E','I','O','U']


def minion_game(sample_string,kevins_score,stuarts_score):

    #  First pass
    #  B,A,N,A,N,A
    #  Second pass
    #  BA,AN,NA,AN,NA
    #  Third pass
    #  BAN,ANA,NAN,ANA
    #  Fourth pass
    #  BANA,ANAN,NANA,

    #  first pass
    # [0,1] [1,2],[2,3],[3,4],[4,5], [5,6]

    #  second pass
    # [0,2], [1,3], [2,4], [3,5], [4,6]

    #  third pass
    # [0,3], [1,4], [2,5], [3,6]

    counter = 1

    while counter <= len(sample_string):
        for index in range(0,len(sample_string)):

            #  This if statement is needed to deal with
            #  slices that go past the final index in the string.
            if index + counter == len(sample_string) + 1:
                break

            # print(str(index),index+counter)
            # print(sample_string[index:index+counter])

            #  Checking to see if substring starts with vowel or
            #  consient.
            if sample_string[index] in vowels:
                kevins_score = kevins_score + 1
            else:
                stuarts_score = stuarts_score + 1

        #  Adding one to counter. This counter will indicate the substring
        #  length.
        counter = counter + 1

    #  Returning scores
    return (kevins_score,stuarts_score)

    
if __name__ == '__main__':
    # s = input()

    kevins_score = 0
    stuarts_score = 0

    (kevins_score,stuarts_score) = minion_game('BANANA',kevins_score,stuarts_score)

    if kevins_score > stuarts_score:
        print('Kevin ' + str(kevins_score))
    elif stuarts_score > kevins_score:
        print('Stuarts ' + str(stuarts_score))
    else:
        print('Draw')
