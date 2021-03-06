“”“
原地算法， 定义两个指针，如果两数字不同，进行保存
”“”
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0  
        i = 0
   
        for j in range(1, len(nums)):
            if  nums[j] != nums[i]:
                i += 1
            nums[i] = nums[j]
            
        return i + 1
                
“”“
利用排序特性遍历删除
”“”
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 1
        while pointer < len(nums):
            if nums[pointer - 1] == nums[pointer]:
                del nums[pointer]
            else:
                pointer += 1
