class Solution:
    def getSecondLargest(self, arr):
        # Code Here if len(nums) < 2:
        if len(arr) < 2:
             return -1

        first = second = -1

        for num in arr:
            if num > first:
                 second = first
                 first = num
            elif first > num > second:
                second = num
        return second if second != -1 else -1