class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        store = set()
        for i,item in enumerate(num):
            if target-item in store:
                index2 = i+1
                break
            else:
                store.add(item)
        index1 = num[:i].index(target-num[i])+1
        return(index1,index2)