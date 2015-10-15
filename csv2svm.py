#!/usr/bin/env python

# vim: ai ts=4 sts=4 et sw=4 ft=python
# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4 filetype=python

'''
SCRIPT converts a CSV file to SVM format
The field separator is ','
All other fields can be textual

Example:

Input CSV:
1,feat1,feat2
-1,feat2,feat3
1,feat4,feat2,feat1

Output SVM:
1 1:1.0 2:1.0
-1 2:1.0 3:1.0
1 4:1.0 2:1.0 1:1.0
'''

import fileinput
import sys

def csv2svm(csvfile):
    d = dict()
    output = list()
    cnt = 1
    for line in fileinput.input():
        tok = line.strip('\n').split(',')
        label = tok[0]
        feats = tok[1:]
        output.append(label)
        for t in feats:
            if t in d.keys():
                output.append( str(d.get(t)) + ':1.0')
            else:
                d[t] = cnt
                cnt = cnt + 1
                output.append( str(d.get(t)) + ':1.0')
        print( " ".join(output) )
        output = list()


def main(args):
    if len(args) < 1:
        print('Usage: mycsv2svm.py <csv>')
        sys.exit(1)

    csvfile = args[0]
    csv2svm(csvfile)

if __name__ == '__main__':
    main(sys.argv[1:])

