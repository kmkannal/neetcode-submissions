class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1 = {}
        seen2 = {}
        for str1 in s:
            seen1[str1] = seen1.get(str1,0)+1
        for str2 in t:
            seen2[str2] = seen2.get(str2,0)+1
        if seen1 == seen2:
            return True
        return False
