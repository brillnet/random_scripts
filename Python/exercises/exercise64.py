from collections import namedtuple
import sys,re

# 5
# ID         MARKS      NAME       CLASS     
# 1          97         Raymond    7         
# 2          50         Steven     4         
# 3          91         Adrian     9         
# 4          72         Stewart    5         
# 5          80         Peter      6   


# Student = namedtuple('ID','MARKS', 'NAME', 'CLASS')
input_list = sys.stdin.readlines()[1:]
list_of_students = []

# Enter your code here. Read input from STDIN. Print output to STDOUT
for line in input_list[1:]:
    
    #  Creating match object to grab appropriate sections of
    #  the line.
    match = re.match('(\d+)\s+(\d+)\s+(\w+)\s+(\d+)',line)
    
    #  Checking match.
    if match:
        print(match.group())