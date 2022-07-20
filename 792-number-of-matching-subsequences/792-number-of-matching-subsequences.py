class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        result = len(words)
        for word in words:
            index = -1
            for w in word:
                index = s.find(w, index + 1)
                if index == -1:
                    result -= 1
                    break
        return result
            
   