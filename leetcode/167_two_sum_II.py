class Solution:
    
    # two pointers
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        
        while l < r:
            temp_sum = numbers[l] + numbers[r]
            
            if temp_sum < target:
                l += 1
            elif temp_sum > target:
                r -= 1
            else:
                return [l+1, r+1]
    # dictionary
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i
