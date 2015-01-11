import copy as copy
@profile
def main():
    x = range(1000000)
    print id(x[1])
    test(copy.deepcopy(x))
def test(y):
    print id(y[1])
    
    

if __name__=="__main__":
    main()