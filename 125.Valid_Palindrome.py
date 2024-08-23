class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = filter(lambda ch: ch.isalnum(), s)
        lowercase_filtered_chars = list(map(lambda ch: ch.lower(), cleaned))

        l = 0
        r = len(lowercase_filtered_chars) - 1
        while l < r:
            if lowercase_filtered_chars[l] != lowercase_filtered_chars[r]:
                return False
            l += 1
            r -= 1
        return True

solution = Solution()
print(solution.isPalindrome(s = "A man, a plan, a canal: Panama"))
print(solution.isPalindrome(s = "race a car"))
print(solution.isPalindrome(s = " "))


        