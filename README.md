# Frequent-Itemsets
This folder file contains the Apriori algorithm and SON algorithm that uses to discover all frenquent itemsets.

Part I - Apriori:

[Input]<br />
The input file is a single line of nested JSON array, within the array, each basket is represented as a JSON array of integers representing item numbers. A sample file is as follows: <br /><br />
[[1, 2], [1, 2, 3], [1, 3, 4], [2, 3, 4], [3, 4]] # 5 baskets <br />

[Output]<br />
Print out candidates and frequent itemsets in each pass, each per line as a SORTED list, until C(k) or L(k) is empty. An example is as follows: <br /><br />
C1: [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]] <br />
L1: [[1], [2], [3], [4], [5], [6]] <br />
C2: [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 3], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6], [4, 5], [4, 6], [5, 6]] <br />
L2: [[1, 2], [1, 3], [2, 3], [2, 6], [3, 5], [4, 5]] <br />
C3: [[1, 2, 3]] <br />
L3: [] <br /><br />

Part II - SON Algorithm:

[Input]<br />
Input of this phase include two parts, one is chunks of baskets the same as phase 1 input, the other is the candidates found in phase 1.

[Output]<br />
One line per each global frequent itemset and its global count, in the following format:<br />
[[1, 2], 18]<br />
[[1, 3], 20]<br />
[[1], 31]<br />
[[2], 22]<br />
[[3], 22]<br />
[[4], 12]<br />
[[6], 15]<br />
[[2, 3], 13]
