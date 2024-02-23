#size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----


import string
alphabet_list = list(string.ascii_lowercase)

def print_line(index):
    print('-'.join(alphabet_list[index:]))

def print_rangoli(size):
    print(alphabet_list[0:size])
    for index in range(0,len(alphabet_list[0:size])):
        print_line(index)
        # your code goes here
        pass

if __name__ == '__main__':
    print_rangoli(5)
    # n = int(input())
    # print_rangoli(n)