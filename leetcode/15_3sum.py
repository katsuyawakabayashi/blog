class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                r, l = i + 1, len(nums) - 1
                while (r < l):
                    sum = nums[i] + nums[r] + nums[l]
                    if sum < 0:
                        r += 1
                    elif sum > 0:
                        l -= 1
                    else:
                        res.append([nums[i], nums[r], nums[l]])
                        r += 1
                        l -= 1
                        while r < l and nums[r] == nums[r - 1]:
                            r += 1
        return res
