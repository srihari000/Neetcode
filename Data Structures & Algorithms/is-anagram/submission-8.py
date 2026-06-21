class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if  len(s) != len(t) :
            return False
        map_s = {}
        map_t = {}
        for i in range(len(s)):
            map_s[s[i]] = map_s.get(s[i], 0) + 1
            map_t[t[i]] = map_t.get(t[i], 0) + 1
        for key in list(map_s.keys()):
            if map_s[key] != map_t.get(key, 0):
                return False
        return True