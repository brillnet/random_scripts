# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
import sys,re

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if attrs:
            self.print_attributes(attrs)
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        if attrs:
            self.print_attributes(attrs)
    def print_attributes(self,attributes_list):
        for index in range(len(attributes_list)):
            print('-> '+attributes_list[index][0] + ' > ' + \
            str(attributes_list[index][1]))
        
#  Getting total number of lines from stdin.
num_lines_of_html = sys.stdin.readline()

line = sys.stdin.readline().strip()
# for index in range(0,int(num_lines_of_html)):
while line:
    #  parser object and feeding each line of html to it
    parser = MyHTMLParser()
    
    #   Checking to see if line is a comment. 
    #   If line starts with <!-- check to see if
    #   line ends with --> If it does skip the line.
    #   If it doesn't continue to read lines until -->
    #   is found at the end of the line. 
    #   Checking end of line re.search(r'-+>$', s)
    if re.match(r'^<!-+', line) and re.search(r'-+>$', line):
        line = sys.stdin.readline().strip()
        continue
        
    #  Need to put the below regexs in some type while loop
    #  Dealing with multilines
    if re.match(r'^<!-+', line) and not re.search(r'-+>$', line):
        line = sys.stdin.readline().strip()
        continue
    
        #  Check to see if next line ends with -->
        if re.search(r'-+>$', line):
            line = sys.stdin.readline().strip()
            continue
    
    parser.feed(line)

