class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for i in range(0,len(nums)):

            if nums[i] in freq:

                freq[nums[i]] += 1

            else:

                freq[nums[i]] = 1

        freq_list = list(freq.items())

        def get_item(item):
            return item[1]


        freq_list = list(freq.items())
    


        freq_list.sort(key=get_item,reverse=True)

        result = []

        for keys in range(k):

            result.append(freq_list[keys][0])

        return result

            
        