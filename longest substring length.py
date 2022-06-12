class Solution:
    def longestSubstring(self, s):
        d = {}
        result = 0
        i=0
        for j in range(len(s)):
            if s[j] in d:
                i = max(i, d[s[j]]+1)

            result = max(result, j-i+1)
            d[s[j]]=j
        return result
solution = Solution()
print(solution.longestSubstring('apple'))