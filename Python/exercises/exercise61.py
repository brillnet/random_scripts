#size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----


import string
alphabet_list = list(string.ascii_lowercase)

def print_line(index,size):
    forward_list = alphabet_list[index:size]
    reverse_list = alphabet_list[index:size][::-1]
    reverse_list.pop()

    #  Creating dashes list
    number_of_dashes = int(((index*2) / 2))
    string_of_dashes = '-' * number_of_dashes

    print(string_of_dashes + '-'.join(reverse_list + forward_list) + \
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
        print_line(index,size)

if __name__ == '__main__':
    print_rangoli(5)