class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {} #seen = set()
        for num in nums:
            if num in seen:
                return True
            seen[num] = True #seen.add(num)
        return False
