class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x == 0:
            return True
        if x<0:
            return False
        else:
            xx = x
        s = xx
        cnt = 0
        while s>=10:
            s = s/10
            cnt +=1
        while cnt>=1:
            head = xx/(10**cnt)
            tail = xx%10
            if head!=tail:
                return False
            
            xx = xx/10-head*(10**(cnt-1))
            cnt -=2
        return True
sol = Solution()

assert(sol.isPalindrome(-101))