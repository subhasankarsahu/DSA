class Solution:
    def pattern5(self, n):
        for i in range(n, 0, -1):
            for j in range(1, i+1):
                print(j, end=" ")

            print()

if __name__ == "__main__":
    sol = Solution()

    n = 5

    sol.pattern5(n)