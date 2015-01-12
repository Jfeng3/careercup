class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        start,end = 0,0
        idict = {}
        rslt = 0
        while end<len(s):
            while 1:
                if end<len(s) and s[end] not in idict:
                    idict[s[end]] = end
                    end +=1
                else:
                    if len(s[start:end])>rslt:
                        rslt = len(s[start:end])
                    break
            if end == len(s):
                break
            tmp = idict[s[end]]+1
            for i in range(start,idict[s[end]]+1):
                idict.pop(s[i],None)
            start = tmp
        return rslt