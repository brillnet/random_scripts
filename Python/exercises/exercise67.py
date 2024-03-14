# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
import sys

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Found a start tag  :", tag)
        print(attrs)
    def handle_endtag(self, tag):
        print("Found an end tag   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Found an empty tag :", tag)
        print(attrs)
        
# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed('<img src="python-logo.png" alt="The Python logo">')
# parser.feed("<html><head><title>HTML Parser - I</title></head>"
#             +"<body><h1>HackerRank</h1><br /></body></html>")

for line in sys.stdin.readlines():
    print(line.strip())