class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        m = {}
        for b in words2:
            for c in b:
                if c not in m or m[c] < b.count(c):
                    m[c] = b.count(c)
        res = []
        for a in list(set(words1)):
            if all(m[k] <= a.count(k) for k in m):
                res += [a]
        return res