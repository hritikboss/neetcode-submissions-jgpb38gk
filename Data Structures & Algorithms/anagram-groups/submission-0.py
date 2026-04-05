class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map=defaultdict(list)
        for s in strs :
            sortedword = ''.join(sorted(s))
            map[sortedword].append(s)
        return list(map.values())