class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        x = 0
        for item in A:
            x = x^item
        return x