class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # a dictionary to store char and last index seen 
        # left pointer points to the beginning of substring, update when we see duplicates
        # right pointer goes through the string
        left=0
        seen={}
        max_length=0

        for right,char in enumerate(s):
            if char in seen and seen[char] >=left: # if current char is duplicate and last time seen index is in the sliding window
                left=seen[char]+1
            seen[char]=right
            max_length=max(max_length,right-left+1)
        return max_length
    

solution=Solution()
print(solution.lengthOfLongestSubstring('abba'))