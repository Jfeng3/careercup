class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        idict = {2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
        current = []
        rslt = []
        self.dfs(idict,digits,0,current,rslt)
        return [ "".join(item) for item in rslt ] 
        
    def dfs(self,idict,digits,k,current,rslt):
        if k ==len(digits):
            rslt.append(current[:])
            return
        char_list = idict[int(digits[k])]
        for char in char_list:
            current.append(char)
            self.dfs(idict,digits,k+1,current,rslt)
            current.pop()