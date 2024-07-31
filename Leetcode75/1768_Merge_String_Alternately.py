class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        min_length = min(len(word1), len(word2))

        res = ''
        for x in range(min_length):
            res += word1[x]
            res += word2[x]
        
        if(min_length == len(word1)):
            for x in range(min_length, len(word2)):
                res += word2[x]
        else:
            for x in range(min_length, len(word1)):
                res += word1[x]
        return res