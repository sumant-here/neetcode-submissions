class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        #put every number in it correct position 
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
        # find the first number that is not in its correct position 
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        # if everything from 1 to n exixts
        return n + 1
        