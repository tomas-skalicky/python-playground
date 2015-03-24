#!/usr/bin/env python3.4

import sys

fooMatches = []
barMatches = []
foobarMatches = []
others = []

for line in sys.stdin:

    lineWithoutEol = line.replace('\n', '')
    insensitiveLine = lineWithoutEol.lower();
    starting_with_foo = insensitiveLine.startswith('foo')
    ending_with_bar = insensitiveLine.endswith('bar')
    
    if starting_with_foo and ending_with_bar:
        foobarMatches.append(lineWithoutEol)
        
    elif starting_with_foo:
        fooMatches.append(lineWithoutEol)
        
    elif ending_with_bar:
        barMatches.append(lineWithoutEol)
        
    else:
        others.append(lineWithoutEol)
    

print('\n--\n'.join(['\n'.join(word) for word in [fooMatches, barMatches, foobarMatches, others]]))
