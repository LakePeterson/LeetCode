##########################################################################
## * Program: twoSum.py
## * Author: Lake Peterson
## * Date: January 14, 2021
## * Description: Given an integer array nums, find the contiguous
## *              subarray (containing at least one number) which has the 
## *              largest sum and return its sum.
##########################################################################

##########################################################################
## * Included Libraries
##########################################################################

from typing import List
import math

##########################################################################
## * Class: Solutions
##########################################################################

class Solutions():

##########################################################################
## * Function: solutionOne
## * Time Complexity: O(n^2)
##########################################################################

    def solutionOne(self, nums: List[int]) -> int:
        maxSum = -math.inf
        currentSum = -math.inf
        for i in range(len(nums)):
            currentSum = nums[i]
            if currentSum > maxSum:
                maxSum = currentSum
            for j in range(i+1, len(nums)):
                currentSum += nums[j]
                if currentSum > maxSum:
                    maxSum = currentSum
        return maxSum

##########################################################################
## * Function: solutionTwo
## * Time Complexity: 
##########################################################################

    def solutionTwo(self, nums: List[int]) -> int:
        maxSum = -math.inf
        currentSum = -math.inf
        for i in range(len(nums)):
            if nums[i] > (currentSum + nums[i]):
                currentSum = nums[i]
            else:
                currentSum = (currentSum + nums[i])
            if currentSum > maxSum:
                maxSum = currentSum
        return maxSum

##########################################################################
## * Function: main
##########################################################################

def main():

    nums = [-2,1,-3,4,-1,2,1,-5,4]

    s = Solutions()

    print(s.solutionOne(nums))
    print(s.solutionTwo(nums))

if __name__ == "__main__":

    main()