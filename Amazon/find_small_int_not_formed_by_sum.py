#link: http://www.careercup.com/question?id=5638615906385920
#desc: Given a array of positive integers, you have to find the smallest positive integer that can not be formed from the sum of numbers from array.
#company: Amazon
#type: Array

def find_small_int_not_formed_by_sum(num):
    if len(num) == 0:
        return 0
    num = sorted(num)
    q = [[0]]
    start = 0
    while q:
        idx = q.pop(0)
        