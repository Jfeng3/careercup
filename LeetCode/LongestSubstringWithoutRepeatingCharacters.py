class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        tail = 0
        head = 1
        maxLen = 0
        set1 = set()
        set1.add(s[0])
        while head<len(s):
            target = s[head]
            if target not in set1:
                set1.add(target)
            else:
                maxLen  = max(maxLen,head-tail)
                while tail<head:
                    if s[tail]==target:
                        tail +=1
                        break
                    else:
                        set1.remove(s[tail])
                        tail +=1
            head +=1
        maxLen  = max(maxLen,head-tail)
        return maxLen