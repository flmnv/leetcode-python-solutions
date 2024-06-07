class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        for word_index in range(len(words)):
            for replace_word in dictionary:
                if words[word_index].startswith(replace_word):
                    words[word_index] = replace_word

        return ' '.join(words)

    # def replaceWords(self, dict: List[str], sentence: str) -> str:
    #     roots = set(dict)
    #     words = sentence.split()
    #     result = []
    #
    #     for word in words:
    #         for i in range(len(word) + 1):
    #             prefix = word[:i]
    #             if prefix in roots:
    #                 result.append(prefix)
    #                 break
    #         else:
    #             result.append(word)
    #
    #     return ' '.join(result)
