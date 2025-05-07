import numpy as np
class Solution(object):
    def longestPalindrome(self, s):
        
    # X=np.array(list("CBABADT"))
    # X=np.array(list("baaaacbd"))
        n=len(s)
        M=[[0 for _ in range(n)] for _ in range(n)]
    
              
        for i in range(n-1,-1,-1):
            M[i][i]=1
            for j in range(i+1,n):
                if s[i]==s[j]:
                    M[i][j]=2+M[i+1][j-1]
                else:
                    M[i][j]=max(M[i+1][j],M[i][j-1])
        print(np.array(M))
        nexti=0
        nextj=n-1
        sol=[]
        while nexti<n and nextj>=nexti:
            if s[nexti]==s[nextj]:
                pos=int(len(sol)/2)
                sol.insert(pos,s[nexti])

                if not nextj==nexti:
                    sol.insert(pos+1,s[nexti])            
                nexti=nexti+1
                nextj=nextj-1
            elif M[nexti][nextj]==M[nexti+1][nextj]:
                nexti=nexti+1
            else:
                nextj=nextj-1
        return M[0][n-1],"".join(sol)
    

sol=Solution()
input="xbcaaaacbd"
input="xbcabcaabda"
M,substr=sol.longestPalindrome(input)
print(M)
print(input,substr)
