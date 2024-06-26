class Solution:
    def reverse(self, x: int) -> int:
        reversed_x = int(str(abs(x))[::-1])

        if reversed_x.bit_length() >= 32:
            return 0

        return -reversed_x if x < 0 else reversed_x
