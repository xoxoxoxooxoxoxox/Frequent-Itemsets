'''
Copyright by Chin-Chwen Tien
Date: Apr. 11 2016
SON Algorithm Part One
'''

import MapReduce
import apriori
import sys
import re

mr = MapReduce.MapReduce()

def mapper(record):

    # call apriori()
    candidates = apriori(record, False)

    # sent local frequent itemsets to intermediate layer
    for i in candidates:
        for c in i:
            mr.emit_intermediate(tuple(c), 1)

def reducer(key, list_of_values):

    # unite local candidates from each chunk
    mr.emit(key)

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)