class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(s, left, right): # expand around center
            while left >= 0 and right < len(s) and s[left] == s[right]: # while left is greater than or equal to 0 and right is less than the length of s and s[left] is equal to s[right]
                left -= 1 # decrement left
                right += 1 # increment right
            return right - left - 1 # return right - left - 1

        max_length = 0 # initialize max_length
        start = 0 # initialize start
        for i in range(len(s)): # loop through the string
            # odd case
            odd_length = expand_around_center(s, i, i) # expand around center
            if odd_length > max_length: # if odd_length is greater than max_length
                max_length = odd_length # set max_length to odd_length
                start = i - (odd_length - 1) // 2 # set start to i - (odd_length - 1) // 2
            # even case
            even_length = expand_around_center(s, i, i + 1) # expand around center
            if even_length > max_length: # if even_length is greater than max_length
                max_length = even_length # set max_length to even_length
                start = i - (even_length - 1) // 2 # set start to i - (even_length - 1) // 2
        return s[start:start + max_length] # return s[start:start + max_length]