class Solution:
    def pattern9(self, n):
        for i in range(1, 2 * n):
            stars = i
            if i > n:
                stars = 2 * n - i
            
            print("* " * stars)
            
        

if __name__ == "__main__":
    sol = Solution()

    n = 5

    sol.pattern9(n)
    
'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
'''