# Given a binary string s ​​​​​without leading zeros,
# return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.

##first approach
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s
    

##second approach
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        count = 0
        for i in range(len(s)):
            if s[i] == '1' and (i == 0 or s[i-1] == '0'):
                count += 1
        return count <= 1