import numpy as np

import random, string

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

class Solution(object):
    def longestPalindrome(self, s):
        
        maxp=1
        n=len(s)
        M_str=[[0 for i in range(n)] for j in range(n)]
        start,end=0,0
   
    
        for i in range(n-1,-1,-1):
            M_str[i][i]=True
            for j in range(i+1,n):
                if s[i]==s[j] and (i==j-1 or M_str[i+1][j-1]):
                    M_str[i][j]=True
                    if j-i+1>maxp:
                      maxp=j-i+1
                      start,end=i,j
                else:
                    M_str[i][j]=False

        return s[start:end+1]
        
#s=randomword(10000)
s="dbabaa"
#s="aa"
sol=Solution()
print(sol.longestPalindrome(s))

def opt(X,i,j):
    if i>j:
        return 0
    if i==j:
        return 1
    a=opt(s,i+1,j-1)
    if X[i]==X[j] and a==j-i-1:
        return 2+a
    b=opt(s,i,j-1)
    c=opt(s,i+1,j)
    return max(a,b,c)

#r=opt(s,0,len(s)-1)
#print(r)
