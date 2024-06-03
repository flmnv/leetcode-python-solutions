class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        start = 0
        substring_cost = 0
        max_length = 0

        for end in range(len(s)):
            substring_cost += abs(ord(s[end]) - ord(t[end]))

            while substring_cost > maxCost:
                substring_cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length
