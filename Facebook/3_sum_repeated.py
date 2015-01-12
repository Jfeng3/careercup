#link: http://www.careercup.com/question?id=5736292639834112
#desc:
#Given an array of integers, return true if there're 3 numbers adding up to zero (repetitions are allowed) 
#{10, -2, -1, 3} -> true 
#{10, -2, 1} -> true -2 + 1 +1 =0
#company: facebook

def three_sum_repeated(num,target):
    num = sorted(num)
    rslt = []
    i = 0
    while i <len(num):
        start = i
        end = len(num)-1
        while start<=end:
            if target == num[i] + num[start] + num[end]:
                rslt.append([num[i],num[start],num[end]])
                start +=1
                while start<=end and num[start-1] == num[start]:
                    start +=1
                end -=1
                while start<=end and num[end] == num[end+1]:
                    end -=1
            elif target > num[i] + num[start] + num[end]:
                start +=1
            else:
                end -=1
        i +=1
        while i<len(num) and (i == 0 or num[i-1] == num[i]):
            i +=1
    return rslt
    
num = [10,-2,1,0,2]
target = 0
print three_sum_repeated(num,target)
            

