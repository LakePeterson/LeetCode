##########################################################################
## * Program: twoSum.py
## * Author: Lake Peterson
## * Date: January 14, 2021
## * Description: Given an array of integers nums and an integer target, 
## *              return indices of the two numbers such that they add up 
## *              to target.
##########################################################################

##########################################################################
## * Included Libraries
##########################################################################

from typing import List

##########################################################################
## * Class: Solutions
##########################################################################

class Solutions():

##########################################################################
## * Function: solutionOne
## * Time Complexity: O(n^2)
##########################################################################

    def solutionOne(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)):
            for j in range (i, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

##########################################################################
## * Function: solutionTwo
## * Time Complexity: O(n)
##########################################################################

    def solutionTwo(self, nums: List[int], target: int) -> List[int]:
        valueDictionary = {}
        for idx, value in enumerate(nums):
            if target - value in valueDictionary:
                return [valueDictionary[target - value], idx]
            else:
                valueDictionary[value] = idx

##########################################################################
## * Function: main
##########################################################################

def main():

    nums = [2,7,11,15]
    target = 9

    s = Solutions()

    print(s.solutionOne(nums, target))
    print(s.solutionTwo(nums, target))

if __name__ == "__main__":

    main()