
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = list()
        result_nodup = set()
        nums = sorted(nums)

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    if (nums[i], nums[l], nums[r]) not in result_nodup:
                        result.append([nums[i], nums[l], nums[r]])
                        result_nodup.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] > 0: # Too big
                    r -= 1
                else:
                    l += 1
        return result