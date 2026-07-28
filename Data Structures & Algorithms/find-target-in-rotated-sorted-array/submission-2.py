class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # if side is sorted and target within range, look there


        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # right is sorted  
            if nums[mid] < nums[right]:
                # target is within right --> look right
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # target is NOT within right --> look left
                else:
                    right = mid - 1
            # left is sorted
            else:
                # target is within left --> look left
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                #target is NOT within left --> look right
                else:
                    left = mid + 1

        return -1

        