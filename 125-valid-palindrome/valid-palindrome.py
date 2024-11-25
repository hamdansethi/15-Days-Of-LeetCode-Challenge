class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        letters = [letter.lower() for letter in s if letter.isalnum()]
        
        return letters == letters[::-1]