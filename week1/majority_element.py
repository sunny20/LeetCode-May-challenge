class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) ==1 :
            return nums[0]
        dic = {}
        majority = int(len(nums)/2)
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] +=1
                if dic[num] > majority:
                    return num
                
                
        