import sys

def print_differences(values_list,set1,set2):
    #  Checking to see what values exist
    #  set1 but not set2 and printing the results
    for val in set1.difference(set2):
        values_list.append(val)
    
    return values_list

set_a_size = sys.stdin.readline()
set_a = set(map(int,sys.stdin.readline().split()))
set_b_size = sys.stdin.readline()
set_b = set(map(int,sys.stdin.readline().split()))

values_list = []

#  Printing out values that exist in set a but not set b.
values_list = print_differences(values_list,set_a,set_b)

#  Printing out values that exist in set b bot not set 1.
values_list = print_differences(values_list,set_b,set_a)

for val in sorted(values_list):
    print(val)

    