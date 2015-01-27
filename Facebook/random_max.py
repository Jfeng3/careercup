"""
http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=114482&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26sortid%3D311
"""
import random
def find_randomMax1(num):
    rslt = []
    cnt = 0
    for i,item in enumerate(num):
        if len(rslt) == 0 or item>num[rslt[0]]:
            rslt = [i]
            cnt = 1
        elif item == num[rslt[0]]:
            cnt +=1
            x = random.sample(range(cnt),1)
            if x[0] == 0:
                rslt = [i]
                
    return random.sample(rslt,1)[0]
    
# o(1) space
def find_randomMax(num):
    pass
num = [2,1,2,1,5,4,5,5]
cnt = 0
for i in range(10000):
    x = find_randomMax1(num)
    if x == 7:
        cnt +=1
print cnt 
            
            