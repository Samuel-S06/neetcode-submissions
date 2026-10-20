class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {} # map nums --> index

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in index_map:
                return [index_map[diff], i]
            else:
                index_map[nums[i]] = i
        
        return []
        