# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
import sys,re

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start : " + tag)
        if attrs:
            self.print_attributes(attrs)
    def handle_endtag(self, tag):
        print("End   : " + tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty : " + tag)
        if attrs:
            self.print_attributes(attrs)
    def print_attributes(self,attributes_list):
        for index in range(len(attributes_list)):
            print('-> '+attributes_list[index][0] + ' > ' + \
            str(attributes_list[index][1]))
    def handle_comment(self,data):
        return
        
#  Getting total number of lines from stdin.
num_lines_of_html = sys.stdin.readline()

#  Reading in line from stdin
line = sys.stdin.readline().strip()

while line:
    
    #  Checking for lines that start with <!-- and don't end with
    #  -->. Reading lines out of sys.stdin.readline() until
    #  line ending in --> is found.
    if re.search(r'<!-+', line) and not re.search(r' -+>', line):
        while not re.search(r'-+>', line):
            line = sys.stdin.readline().strip()
            continue

    #  parser object and feeding each line of html to it
    parser = MyHTMLParser()
    parser.feed(line)
    line = sys.stdin.readline().strip()