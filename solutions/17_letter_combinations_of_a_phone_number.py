class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        def create_combinations(combination: str, combinations: list[tuple]):
            if len(combinations) == 1:
                return [combination + char for char in combinations[0]]

            result = []
            for char in combinations[0]:
                result.extend(create_combinations(combination + char, combinations[1:]))

            return result

        letters = {
            '2': ('a', 'b', 'c'),
            '3': ('d', 'e', 'f'),
            '4': ('g', 'h', 'i'),
            '5': ('j', 'k', 'l'),
            '6': ('m', 'n', 'o'),
            '7': ('p', 'q', 'r', 's'),
            '8': ('t', 'u', 'v'),
            '9': ('w', 'x', 'y', 'z')
        }

        combination_list = [letters[digit] for digit in digits]
        return create_combinations('', combination_list)
