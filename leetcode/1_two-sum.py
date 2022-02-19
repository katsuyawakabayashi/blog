class Solution:
    # brute force
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
    
    # dictionary
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            compl = target - nums[i]
            if compl in dic:
                return [i, dic[compl]]
            else:
                dic[nums[i]] = i
