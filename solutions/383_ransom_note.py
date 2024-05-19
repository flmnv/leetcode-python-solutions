class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False

        for _ in range(len(ransomNote)):
            magazine_index = magazine.find(ransomNote[0])
            if magazine_index == -1:
                return False
            ransomNote = ransomNote[1:]
            magazine = magazine[:magazine_index] + magazine[magazine_index + 1:]

        return True
