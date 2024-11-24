# Given an integer array nums, return true if there exists a 
# triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
#  If no such indices exists, return false.


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first = second = float('inf')

        for x in nums:
            if x <= first: # while X is the lowest, evaluate the next value
                first = x
            elif x <= second:
                second = x
            else:
                return True
            
        return False