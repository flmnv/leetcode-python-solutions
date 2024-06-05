class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []

        chars = set(words[0])
        for char in chars:
            char_count = float('inf')

            for word in words:
                char_count = min(word.count(char), char_count)
                if char_count == 0:
                    break

            result.extend([char] * char_count)

        return result
