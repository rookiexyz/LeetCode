class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: # if numRows is 1, return the original string
            return s # return the original string
        rows = [''] * numRows # create a list of empty strings
        index, step = 0, 1 # initialize the index and step
        for c in s: # for each character in the string
            rows[index] += c # add the character to the current row
            if index == 0: # if the current row is the first row 
                step = 1 # set the step to 1
            elif index == numRows - 1: # if the current row is the last row
                step = -1 # set the step to -1
            index += step # increment the index by the step
        return ''.join(rows) # return the joined string