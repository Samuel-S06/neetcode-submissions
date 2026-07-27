class Solution:
    def findMin(self, nums: List[int]) -> int:
        # modified BS
        # if left < mid and mid >right --> search right
        # if left > mid and mid < right --> search left

        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2
            
            # if array is sorted, return min
            if nums[left] < nums[right]:
                return nums[left]

            if nums[mid] < nums[right]:
                right = mid
            else: 
                left = mid + 1
        
        return nums[left]


