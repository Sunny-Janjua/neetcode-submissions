class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap=defaultdict(list)

        for char in strs:
            count=[0]*26
            for newchar in char:

                count[ord(newchar)-ord("a")]+=1
            
            hashmap[tuple(count)].append(char)

        return list(hashmap.values())