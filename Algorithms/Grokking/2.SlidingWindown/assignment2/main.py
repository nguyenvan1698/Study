#Problem Statement #
#Given an array of positive numbers and a positive number ‘S’, find the length
#of the smallest contiguous subarray whose sum is greater than or equal to
#‘S’. Return 0, if no such subarray exists.


import math
class MaxSumSubArrayOfSizeK:
    def maxSum(self,arr,k):
        lenght = len(arr)
        windownSum = 0
        sizeOfSubArray = 0
        minSize = len(arr)
        right = 0
        while right < lenght:
           windownSum += arr[right]
           sizeOfSubArray +=1

           while windownSum >=k:
               minSize = min(sizeOfSubArray,minSize)
               windownSum -= arr[right-k]
               sizeOfSubArray -=1

           right +=1
        return minSize

test = MaxSumSubArrayOfSizeK()
arr =[2, 1, 5, 2, 8]
print(test.maxSum(arr,7 ))