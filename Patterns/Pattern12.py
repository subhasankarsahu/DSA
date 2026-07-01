class Solution:
    def pattern12(self, n):
        num = 1
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(num, end=" ")
                num = num + 1

            print()
        

if __name__ == "__main__":
    sol = Solution()

    n = 5

    sol.pattern12(n)
    
'''
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
'''