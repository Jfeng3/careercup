"""
link http://www.careercup.com/question?id=5863307617501184
Given a array of positive integers, find all possible triangle triplets that can be
formed from this array. 
eg: 9 8 10 7 
ans: 9 8 10, 9 8 7, 9 10 7, 7 8 10 
Note : array not sorted, there is no limit on the array length
"""
def find_all_triangle_triples(num):
    if len(num) == 0:
        return []
    rslt = []
    num = sorted(num)
    