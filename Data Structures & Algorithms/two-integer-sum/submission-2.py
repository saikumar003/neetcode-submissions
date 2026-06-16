class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq={}
        for i in range(len(nums)):
            
            rem = target - nums[i]

            if rem in freq:
                return [freq[rem],i]

            freq[nums[i]] = i
        