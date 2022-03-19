class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        max_length = 0
        start = 0
        for i in range(len(s)):
            # odd case
            odd_length = expand_around_center(s, i, i)
            if odd_length > max_length:
                max_length = odd_length
                start = i - (odd_length - 1) // 2
            # even case
            even_length = expand_around_center(s, i, i + 1)
            if even_length > max_length:
                max_length = even_length
                start = i - (even_length - 1) // 2
        return s[start:start + max_length]

