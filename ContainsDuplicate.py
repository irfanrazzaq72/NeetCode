"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate={}
        for num in nums:
            if num in duplicate:
                duplicate[num] +=1
            else:
                duplicate[num] =1
        for num, count in duplicate.items():
            if  count >1:
                return True
                break
        return False
            
