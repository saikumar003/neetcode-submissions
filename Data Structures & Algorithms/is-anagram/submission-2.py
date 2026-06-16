from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0]*26 # space O(1) fixed size
        for ch_s,ch_t in zip(s,t):
            count[ord(ch_s) - ord ('a')] += 1
            count[ord(ch_t) - ord('a')] -= 1
            

        for c in count:
            if c != 0 :
                return False

        return True



        # if len(s)!= len(t):
        #     return False
        # #Time Complexity  O(n)
        # # space Complexity O(N)
        # s_counter = Counter(s)
        # t_counter = Counter(t)
        # return s_counter == t_counter