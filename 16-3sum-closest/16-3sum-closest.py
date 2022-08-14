class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3: return nums[0] + nums[1] + nums[2]
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        
        for left in range(len(nums)-2):
            mid, right = left+1, len(nums)-1
            if left > 0 and nums[left] == nums[left-1]: continue
            while mid < right:
                sm = nums[left] + nums[mid] + nums[right]
                if sm == target: return sm 
                if abs(sm-target) < abs(res-target):
                    res = sm
                if sm > target:
                    right -= 1
                else:
                    mid += 1 
                
        return res