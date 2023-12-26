class Solution(object):
    def containsDuplicate(self, nums):
        newValues = set(nums)
        if len(nums) != len(newValues):
            return True
        else:
            return False
        