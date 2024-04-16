class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n=len(text1)
        m=len(text2)
        M=[[0 for _ in range(m+1)] for _ in range (n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                si,sj=i-1,j-1
                if text1[si]==text2[sj]:
                    M[i][j]=1+M[i-1][j-1]
                else:
                    M[i][j]=max(M[i-1][j],M[i][j-1])

        return M[n][m]
    

sol=Solution()
print(sol.longestCommonSubsequence("aabdc","abcd"))