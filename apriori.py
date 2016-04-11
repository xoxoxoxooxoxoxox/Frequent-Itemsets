'''
Copyright by Chin-Chwen Tien
Date: Apr. 11 2016
'''

import json
import sys
import re
from itertools import combinations

def apriori(baskets, prRst):

	Ctable = {}
	C = []
	L = []
	freItemset = [] # return list
	numOfBuckets = 0
	k = 1
	
	# phase one 
	# generate count table (C1)
	for b in baskets:
		numOfBuckets += 1
		for item in b:
			Ctable.setdefault(item, 0)
			Ctable[item] += 1

	# calculate support threshold
	sup = numOfBuckets * 0.3

	# convert into frequent-items table (L1)
	for key in Ctable:
		C.append([key])
		if Ctable[key] >= sup:
			L.append([key])

	# print C1 and L1 if prRst is true
	if prRst:
		print "C" + str(k) + ":", C
		print "L" + str(k) + ":", L

	# store L1
	freItemset.append(L)

	# run phase k where k is greater than 1
	while C and L:

		# phase k
		k += 1

		# produce candidate pairs - Ck
		Ctable = {}		
		C = []
		for i in range(0, len(L) - 1):
				for j in range(i + 1, len(L)):
					if cmp(L[i][0 : k - 2], L[j][0 : k - 2]) == 0:
						checkSubset = 0
						pair = L[i] + L[j][k - 2 : ]
						for p in combinations(pair, k - 1):
							if list(p) in L:
								checkSubset += 1
						if checkSubset == k:
							Ctable.setdefault(tuple(pair), 0)
							C.append(pair)

		# count candidate pairs
		for b in baskets:
			if len(b) >= k:
				b.sort()
				for pair in combinations(b, k):
					if(Ctable.has_key(pair)):
						Ctable[pair] += 1

		# produce frequent k-itemsets - Lk
		L = []
		for pair in Ctable:
			if Ctable[pair] >= sup:
				L.append(list(pair))

		# check both C and L are whether empty or not, so it won't print empty result
		if not C and not L:
			break

		# sort Ck and Lk
		C.sort()
		L.sort()

		# print Ck and Lk if prRst is true
		if prRst:
			print "C" + str(k) + ":", C
			print "L" + str(k) + ":", L

		# store Lk
		if L:
			freItemset.append(L)

	return freItemset

if __name__ == '__main__':
	inputdata = open(sys.argv[1])
	for line in inputdata:
		baskets = json.loads(line)
		baskets.sort()
	apriori(baskets, True)