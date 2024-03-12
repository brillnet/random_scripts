# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def check_set(count,initial_set,comparison_set,set_type):

    #  If list_type is 'a' and val is in comparison list
    #  a point is added to the total count.
    if set_type == 'a':

        #  Getting the total number of intersections
        count = len(initial_set.intersection(comparison_set))
        return count
    else:
        #  If list_type is 'b' and val is in comparison list
        #  a point is added to the total count.
        length_of_negatives = len(initial_set.intersection(comparison_set))
        count = count - length_of_negatives
    return count
    
#  This counter will keep track of the score.       
count = 0

n_and_m_set = sys.stdin.readline().strip().split()
initial_set = sys.stdin.readline().strip().split()
a_set = sys.stdin.readline().strip().split()
b_set = sys.stdin.readline().strip().split()


# zip the two lists together to create a list of key-value pairs
key_value_pairs = zip(keys, values)

count = check_set(count,initial_set,a_set,'a')
count = check_set(count,initial_set,b_set,'b')

print(count)