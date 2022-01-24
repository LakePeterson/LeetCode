Maximum Subarray Problem Link: https://leetcode.com/problems/maximum-subarray/

Solution One Explanation:

The first solution requires two nested loops, where the outer loops over all of the elements of the given list. The inner loop starts iterating one spot after the ccurrent index, from which it calculates what the largest sum is from given index. From here I calculate the largest sum value starting at the outer loop index value.

Solution Two Explanation:

The second solution is a faster approach where we eliminate one of the loops, to avoid any unnecessary iterations. Instead this time I am taking the max value between the current index and the current sum value. If the current index value is larger then we replace the current sum value with the current index value. If it is not larger then the current sum value and the current index value will be added together. The maxSum value should now be updated, and in the end the largest sum will have been found.