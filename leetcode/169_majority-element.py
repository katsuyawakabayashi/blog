class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        maj_num = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == maj_num:
                count += 1
            else:
                if count == 0:
                    count += 1
                    maj_num = nums[i]
                    
                else: 
                    count -= 1
                    if count == 0:
                        maj_num = nums[i]
                
        return maj_num
