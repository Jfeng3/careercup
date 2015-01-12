class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        dp  = [ 0 for i in range(len(s)) ] 
        dp[-1] = 1
        for i in range(len(s)-2,-1,-1):
            x = dp[i+1]
            if s[i] in s[i+1:i+x+1]:
                index = s[i+1:i+x+1].index(s[i])
                dp[i] = index+1
            else:
                dp[i] = dp[i+1]+1
        return max(dp)