class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_map = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in string_map:
                string_map[sorted_s] = []
            string_map[sorted_s].append(s)

        return list(string_map.values())