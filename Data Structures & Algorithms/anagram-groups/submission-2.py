class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagrams = {}

        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char)-ord('a')] += 1
            
            key_tuple = tuple(key)
            if key_tuple in anagrams:
                anagrams[key_tuple].append(word)
            else:
                anagrams[key_tuple] = [word]
        
        for k,v in anagrams.items():
            result.append(v)

        return result
            
        
        