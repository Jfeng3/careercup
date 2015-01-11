#2. In a cartesian plane, there are N tanks and M objects placed. Tanks can fire in 4 directions (N, S, E, W). Position of tanks and objects are given as input and are fixed. We have to find a way to give directions to N tanks such that they will not hit any object and any other tanks. If a tank can fire in 2 directions, then a direction whose ASCII code is lesser will be given preference.Example:-
#Input :-
#N=2
#M=3
#
#Position of tanks
#(0,0)
#(1,1)
#
#Position of Objects
#(0,2)
#(0,-2)
#(-2,0)
#
#Direction of N tanks should be :-
#(0,0) E -> This tank should fire in east direction
#(1,1) E -> This tank can fire in all 4 directions. Since E has least ASCII code in all 4 of them, so E

def find_direction(N,M,tanks,obstacles):
    rslt = {}
    all_obj = tanks + obstacles
    for tank in tanks:
        tank_idx = all_obj.index(tank)
        rest_obj = all_obj[:tank_idx]+all_obj[tank_idx+1:]
        for direction in ['E','N','S','W','X']:
            if direction == 'X':
                print "no solution"
            i = 0
            while i < len(rest_obj):
                if onDirection(tank,rest_obj[i],direction):
                    break
                i +=1
            if i == len(rest_obj):
                rslt[tank] = direction
                break
    return rslt
            
                
    
def onDirection(obj1,obj2,dd):
    # return True is obj2 is on obj1's dd direction
    if dd == 'E':
        return obj1[0] == obj2[0] and obj2[1]>obj1[1]
    elif dd == 'N':
        return obj1[1] == obj2[1] and obj2[0]>obj1[0]
        
    elif dd == 'S':
        return obj1[1] == obj2[1] and obj2[0]<obj1[0]
    elif dd == 'W':
        return obj1[0] == obj2[0] and obj2[1]<obj1[1]
        
tanks = [(0,0),(1,1)] 
obstacles = [(0,2),(0,-2),(-2,0)]
print find_direction(2,3,tanks,obstacles)  