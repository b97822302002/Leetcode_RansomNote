class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        for letter in ransomNote:    
            if letter in list(magazine):              
                list(magazine).remove(letter)               
            else:
                return False
        return True
