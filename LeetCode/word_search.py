class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])
        current = [[ False for i in range(n)] for j in range(m) ] 
        board = [ [x for x in item] for item in board] 
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    current[i][j] = True
                    if self.exist_re(board,m,n,word,1,current,i,j):
                        return True
                    current[i][j] = False
        return False
        
    def exist_re(self,board,m,n,word,k,current,i,j):
        if k == len(word):
            return True
        for item in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            if (item[0]>=0 and item[0]<m and item[1]>=0 and item[1]<n) and current[item[0]][item[1]] == False and board[item[0]][item[1]]==word[k]:
                current[item[0]][item[1]] = True
                if self.exist_re(board,m,n,word,k+1,current,item[0],item[1]):
                    return True
                current[item[0]][item[1]] = False
        return False
        
        
        
    def isValid(self,m,n,i,j):
        return i>=0 and i<m and j>=0 and j<n