from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for word in strs:
            count = [0]*26
            for ch in word:
                count[ord(ch) - ord('a')]+=1

            key = tuple(count)
            anagram_dict[key].append(word)
        return list(anagram_dict.values())
        