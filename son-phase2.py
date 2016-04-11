'''
Copyright by Chin-Chwen Tien
Date: Apr. 11 2016
SON Algorithm Part Two
'''

import MapReduce
import sys
import re
import json
from itertools import combinations

mr = MapReduce.MapReduce()

def mapper(record):

    # 2nd input - candidates
    phase1output = open(sys.argv[2])

    # count the occurence of each frequent itemset candidates from phase1output in each chunk
    for line in phase1output:
        candidate = json.loads(line)
        numOfBaskets = 0
        count = 0
        for basket in record:
            basket.sort()
            numOfBaskets += 1
            for pair in combinations(basket, len(candidate)):
                if tuple(candidate) == pair:
                    count += 1
        mr.emit_intermediate(tuple(candidate), (count, numOfBaskets))

def reducer(key, list_of_values):

    # key: frequent itemsets
    # value: global count
    count = 0
    totalOfBaskets = 0

    for localCount in list_of_values:
        count += localCount[0]
        totalOfBaskets += localCount[1]

    if count >= (totalOfBaskets * 0.3):
        mr.emit((key, count))

if __name__ == '__main__':

    # 1st input - chunks
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)