# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def check_list(count,initial_list,comparison_list,list_type):
    for val in initial_list:
        #  If list_type is 'a' and val is in comparison list
        #  a point is added to the total count.
        if list_type == 'a':
            if val in comparison_list:
                count = count + 1
        else:
        #  If list_type is 'b' and val is in comparison list
        #  a point is added to the total count.
            if val in comparison_list:
                count = count - 1

    return count
    
#  This counter will keep track of the score.       
count = 0

n_and_m_list = sys.stdin.readline().strip().split()
initial_list = sys.stdin.readline().strip().split()
a_list = sys.stdin.readline().strip().split()
b_list = sys.stdin.readline().strip().split()

count = check_list(count,initial_list,a_list,'a')
count = check_list(count,initial_list,b_list,'b')

print(count)