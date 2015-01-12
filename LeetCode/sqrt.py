class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x == 0:
            return 0
        if x == 1 or x == 2 or x == 3:
            return 1
        else:
            start,end = 1,x
            while start<end:
                print start,end
                if start+1 == end:
                    if x/end >=end:
                        return end
                    else:
                        return start
                mid = (start+end)/2
                if x/mid>=mid:
                    start = mid
                elif x/mid<mid:
                    end = mid

sol = Solution()
x = 4
sol.sqrt(x)