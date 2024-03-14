from html.parser import HTMLParser
import sys

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
        
# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
num_lines_of_html = sys.stdin.readline()

for html_line in range(0,int(num_lines_of_html)):
    #  parser object and feeding each line of html to it
    parser = MyHTMLParser()
    parser.feed(sys.stdin.readline().strip())
