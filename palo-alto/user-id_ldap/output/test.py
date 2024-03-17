#!/usr/bin/python3
import sys
input = open(sys.argv[-1])
output = open("/output/foobar.out", "a")
for line in input:
    output.write(line)
output.close