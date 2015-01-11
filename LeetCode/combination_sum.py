class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates = sorted(candidates)
        rslt = []
        current = []
        self.combinationSum_re(candidates,target,0,current,rslt)
        return rslt
        
    def combinationSum_re(self,candidates,target,k,current,rslt):
        if k == len(candidates):
            if target == 0:
                rslt.append(current[:])
            return
        if target<0:
            return
        self.combinationSum_re(candidates,target,k+1,current,rslt)
        current.append(candidates[k])
        self.combinationSum_re(candidates,target-candidates[k],k,current,rslt)
        current.pop()