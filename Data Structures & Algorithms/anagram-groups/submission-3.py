from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for word in strs:
            count = [0]*26
            for ch in word:
                count[ord(ch) - ord('a')]+=1
            #Time Complexity is O(N*M)
            #Space Complexity is O(N*M)
            key = tuple(count)
            anagram_dict[key].append(word)
        return list(anagram_dict.values())
# -----------------------------------------------------------------------
#         #Brute Force 
#         for word in strs:
#             key=''.join(sorted(word)) #Sorting a string of length m takes O(m log m) time.
#             anagram_dict[key].append(word)
#         return list(anagram_dict.values())

# ---------------------------------------------------------------------------------
# Time: O(n * (m log m)) You have n strings, and for each string s, the time complexity is O(m log m).

# Thus, the overall time complexity is:
# O(n * m log m)
# Space: O(n * m) The space for the dictionary is O(n * m).

# The space for sorting each string is O(m), but it's temporary and reused for each string.

# Thus, the overall space complexity is:
# O(n * m)
# n is the number of strings, m is the length of largest string

        