class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        open_parentheses = []
        for char in s:
            if char in parentheses:
                open_parentheses.append(char)
            elif not open_parentheses or parentheses[open_parentheses.pop()] != char:
                return False

        return len(open_parentheses) == 0
