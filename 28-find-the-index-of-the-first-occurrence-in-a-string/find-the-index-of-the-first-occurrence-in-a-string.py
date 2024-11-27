import re

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        match = re.search(needle, haystack)
        
        if not match:
            return -1
        else: 
            return match.start() 