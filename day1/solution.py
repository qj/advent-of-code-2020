import os 
import sys

class Solution:

    def get_input(self, file_name):
        with open(os.path.join(sys.path[0], file_name), "r") as f:
            return f.read().split()

    def two_sum(self, nums, target):
        nums = [int(n) for n in nums]
        seen = {}
        for n in nums:
            if target - n in seen:
                return (n, target - n)
            seen[n] = 1
        return None, None

    def three_sum(self, nums, target):
        nums = [int(n) for n in nums]
        for i in range(len(nums)):
            n1, n2 = self.two_sum(nums[i + 1:], target - nums[i])
            if n1:
                return (nums[i], n1, n2)


if __name__ == '__main__':
    s = Solution()
    nums = s.get_input("input.txt")
    print(s.two_sum(nums, 2020))
    print(s.three_sum(nums, 2020))