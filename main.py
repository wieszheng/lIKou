class Solution:
    def twoSum(self, nums, target):
        """
        给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
        你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
        """
        for i in range(len(nums)):
            res = target - nums[i]
            if res in nums[i + 1:]:
                return [i, nums[i + 1:].index(res) + i + 1]

    def isPalindrome(self, x):
        """
        给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
        回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
        例如，121 是回文，而 123 不是。
        """
        if x < 0:
            return False
        if x % 10 == 0:
            return False
        if x < 10:
            return True
        res = 0
        while x > res:
            res = res * 10 + x % 10
            x = x // 10
        return x == res or x == res // 10

    def uniqueNumber(self, nums):
        res = 0
        for i in range(len(nums)):
            res ^= nums[i]
        return res
nums = [1,2,3,4,8,4,3,2,12]
print(Solution().uniqueNumber(nums))


