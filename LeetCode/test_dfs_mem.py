@profile
def main():
    dfs(5000,[])
    
    
def dfs(k,current):
    if len(current) > k:
        return
    else:
        dfs(k,current+range(1000))
        dfs(k,current+range(2000,3000))
      
def dfs2(k,current):
    if len(current) > k:
        return
    else:
        for i in range(1000):
            current.append(i)
        dfs2(k,current)
        for i in range(1000):
            current.pop()
        for i in range(2000,3000):
            current.append(i)
        dfs2(k,current)
        for i in range(1000):
            current.pop()
        
if __name__=="__main__":
    main()
    