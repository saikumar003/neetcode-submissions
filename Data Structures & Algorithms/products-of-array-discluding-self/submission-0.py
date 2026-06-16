""" prerequisite for this 

1. Arrays and Traversal

You should be comfortable with:

nums = [1, 2, 3, 4]

for i in range(len(nums)):
    print(nums[i])

Know:

Forward traversal
Reverse traversal
Reading and updating array elements
2. Running Sum Pattern

Example:

nums = [1, 2, 3, 4]

running_sum = 0

for num in nums:
    running_sum += num

This teaches the idea of carrying information from previous elements.

3. Prefix Sum Pattern

Example:

nums = [1, 2, 3, 4]

prefix = [0] * len(nums)

running_sum = 0

for i in range(len(nums)):
    running_sum += nums[i]
    prefix[i] = running_sum

Output:

[1, 3, 6, 10]

This is usually the first "array preprocessing" pattern people learn.

4. Suffix Sum Pattern

You've already asked about this.

nums = [1,2,3,4]

Output:

[10,9,7,4]

nums = [1, 2, 3, 4]

suffix = [0] * len(nums)

running_sum = 0

for i in range(len(nums)-1, -1, -1):

    running_sum += nums[i]

    suffix[i] = running_sum

print(suffix)

Output:

[10, 9, 7, 4]

This teaches traversing from right to left while maintaining state.

5. Prefix Product Pattern

Instead of sums, multiply.

nums = [1,2,3,4]

prefix = [1] * len(nums)

product = 1

for i in range(len(nums)):
    prefix[i] = product
    product *= nums[i]

Output:

[1,1,2,6]

Meaning:

Elements before index 0 = 1
Elements before index 1 = 1
Elements before index 2 = 1×2 = 2
Elements before index 3 = 1×2×3 = 6
6. Suffix Product Pattern
nums = [1,2,3,4]

suffix = [1] * len(nums)

product = 1

for i in range(len(nums)-1, -1, -1):
    suffix[i] = product
    product *= nums[i]

Output:

[24,12,4,1]


"""





class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)

        prefix = 1

        for i in range(len(nums)):

            result[i] = prefix

            prefix *= nums[i]
        
        suffix = 1

        for i in range(len(nums)-1,-1,-1):

            result[i] *=  suffix

            suffix *= nums[i] 

        return result