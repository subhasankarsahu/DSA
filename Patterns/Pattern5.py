class Solution:
    def pattern5(self, n):
        for i in range(n+1):
            for j in range(n-i+1):
                print("* ", end=" ")

            print()

if __name__ == "__main__":
    sol = Solution()

    n = 5

    sol.pattern5(n)

'''
*  *  *  *  *  *  
*  *  *  *  *  
*  *  *  *  
*  *  *  
*  *  
* 
'''