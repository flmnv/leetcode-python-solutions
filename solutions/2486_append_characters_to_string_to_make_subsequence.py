class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_length = len(t)

        t_index = 0
        for s_char in s:
            if s_char == t[t_index]:
                t_index += 1
                if t_index >= t_length:
                    return 0

        return t_length - t_index
