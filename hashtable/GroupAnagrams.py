class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #2025-10-19
        # map sorted anagram to list of anagrams
        anagrams = {}

        for s in strs:
            sortedS = tuple(sorted(s))
            if sortedS in anagrams:
                anagrams[sortedS].append(s)
            else:
                anagrams[sortedS] = [s]

        result = []

        for anagram in anagrams:
            result.append(anagrams[anagram])
        
        return result


        


