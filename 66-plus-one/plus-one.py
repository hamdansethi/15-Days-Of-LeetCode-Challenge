class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = int(''.join(map(str, digits)))
        num = list(str(number + 1))
        return list(map(int, num))
