#Problem Statement #
#Given an array of positive numbers and a positive number ‘k’, find the
#maximum sum of any contiguous subarray of size ‘k’
import math
class MaxSumSubArrayOfSizeK:
    def maxSum(self,arr,k):
        lenght = len(arr)
        windownSum = 0
        maxSum = 0
        right = 0
        while right < lenght:
           windownSum += arr[right]

           if right > (k-1):
               windownSum -= arr[right-k]
               maxSum = max(windownSum,maxSum)
           right +=1
        return maxSum

#main
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
test = MaxSumSubArrayOfSizeK()
print('the maximum result is:')
print(test.maxSum(arr,4))








