class Solution:
    def longestPalindrome(self, s: str) -> int:
        unique_chars_count = defaultdict(int)
        longest_palindrome_length = 0

        for char in s:
            unique_chars_count[char] += 1

        middle_single_char = False
        for char_count in unique_chars_count.values():
            if char_count % 2:
                middle_single_char = True

            if char_count > 2 and char_count % 2:
                longest_palindrome_length += char_count - middle_single_char
            elif char_count % 2 == 0:
                longest_palindrome_length += char_count

        if middle_single_char:
            longest_palindrome_length += 1

        return longest_palindrome_length

    # def longestPalindrome(self, s: str)  -> int:
    #     unique_chars_count = defaultdict(int)
    #     odd_count = 0

    #     for char in s:
    #         unique_chars_count[char] += 1
    #         if unique_chars_count[char] % 2 == 1:
    #             odd_count += 1
    #         else:
    #             odd_count -= 1

    #     return len(s) - odd_count + 1
