class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        zip_strs = tuple(zip(*strs))
        for i, zip_str in enumerate(zip_strs):
            if len(set(zip_str)) != 1:
                return strs[0][:i]

        if not zip_strs:
            return ''

        return strs[0][:len(zip_strs)]
