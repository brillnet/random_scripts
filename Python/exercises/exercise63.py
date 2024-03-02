# STDIN       Function
# -----       --------
# AABCAAADA   s = 'AABCAAADA'
# 3           k = 3

# AB
# CA
# AD

def merge_the_tools(string,k):

    sample_dictionary = {}

    for index in range(len(string)):
        #  First pass
        #  0,3
        #  Second pass
        #  3,6
        #  Third pass
        #  6,9
        if index == 0:
            sample_dictionary[index] = index + k
            print_non_duplicates(set(string[index:index+3]))
        elif index in sample_dictionary.values():
            sample_dictionary[index] = index + k
            print_non_duplicates(set(string[index:index+3]))
        else:
            pass
    

def print_non_duplicates(no_duplicates_set):
    print(''.join(no_duplicates_set))

        #  Criteria for filling dictionary
        # 0,3,6,9

sample_string = 'AABCAAADA'
string_length = 3

merge_the_tools(sample_string,string_length)