#size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----


import string
alphabet_list = list(string.ascii_lowercase)
final_picture_list = []

def print_picture():
    #  Printing first half of picture
    for line in final_picture_list[::-1]:
        print(line)
    
    #  Printing second half of picture
    for line in final_picture_list[1:]:
        print(line) 

def fill_final_picture_list(index,size):
    #  Creating list of letters in regular order [a,b,c]
    forward_list = alphabet_list[index:size]
    #  Creating list of letters in reverse order [c,b,a]
    reverse_list = alphabet_list[index:size][::-1]
    #  Popping off last element in reverse list. [c,b]
    reverse_list.pop()

    #  Getting total number of dashes that will exist
    #  at front and back of list.
    number_of_dashes = int(((index*4) / 2))
    string_of_dashes = '-' * number_of_dashes

    #  Filling final picture list.
    final_picture_list.append(string_of_dashes +\
                    '-'.join(reverse_list + forward_list) + \
                        string_of_dashes)

    if number_of_dashes == 0:
        pass
    else:
        line_without_dashes = '-'.join(reverse_list + forward_list)
        # print(line_without_dashes)
        # print(string_of_dashes +  line_without_dashes + string_of_dashes)
        # if index == 0 dashes * 2 
        # if index == 1 dashes * 2 = --
        # if index == 2 dashes * 2 = ----
        # if index == 3 dashes * 2 = ------
        # if index == 5 dashes * 2 = ----------
        # if index == 7 dashes * 2 = --------------

def print_rangoli(size):
    for index in range(0,len(alphabet_list[0:size])):
        fill_final_picture_list(index,size)

    #  Printing final picture.
    print_picture()
if __name__ == '__main__':
    print_rangoli(5)