
class Solution:
    def validPalindrome(self, s: str):
        def isPalindrome(s: str, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        l = 0 
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return isPalindrome(s, l + 1, r) or isPalindrome(s, l, r - 1)
            l += 1
            r -= 1
        return True

solution = Solution()
print(solution.validPalindrome(s = "aba"))

print(solution.validPalindrome(s = "abca"))

print(solution.validPalindrome(s = "abc"))