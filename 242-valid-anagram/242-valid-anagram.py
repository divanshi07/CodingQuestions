class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {i : s.count(i) for i in set(s)}
        
        dict2 = {i : t.count(i) for i in set(t)}
        if(len(dict1)>len(dict2)):
            return False
        for key,value in dict2.items():
            if key not in dict1 or dict2[key]<dict1[key]:
                return False
        return True