class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = {}
        for c in s1:
            s1Map[c] = 1 + s1Map.get(c, 0)
        need = len(s1Map)
        for i in range(len(s2)):
            s2Map, cur = {}, 0
            for j in range(i, len(s2)):
                s2Map[s2[j]] = 1 + s2Map.get(s2[j], 0)
                if s1Map.get(s2[j], 0) < s2Map[s2[j]]:
                    break
                if s1Map.get(s2[j], 0) == s2Map[s2[j]]:
                    cur += 1
                if cur == need:
                    return True 

        
        return False
        