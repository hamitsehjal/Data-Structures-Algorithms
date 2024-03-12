'''
Import List module
'''
from typing import List


class Solution:
    '''
    Solution Class
    '''

    def running_sum(self, nums: List[int]) -> List[int]:
        '''
        Calculate the cumulative sum of 1D Array
        '''
        for i in range(1, len(nums)):
            nums[i] = nums[i]+nums[i-1]

        return nums


# Test-Case
input1 = [1, 2, 3, 4, 5, 6]
solution_instance = Solution()
print(solution_instance.running_sum(input1))
input2 = [1, 1, 1, 1, 1, 1]
print(solution_instance.running_sum(input2))
