class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        all_triples = []
        
        def twoSum(i, target, all_triples):
            l, r = i + 1, len(nums) - 1

            while l < r:
                sum = nums[l] + nums[r]

                if sum == target:
                    all_triples.append([-target, nums[l], nums[r]])

                    # skips dups inner loop
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    
                    # since we need to find all unique pairs = target
                    l += 1
                    r -= 1
                elif sum > target:
                    r -= 1
                elif sum < target:
                    l += 1
            
        for i in range(len(nums) - 2):
            # skip dups main loop
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            # x + y = -target
            twoSum(i, target, all_triples)

        return all_triples

        