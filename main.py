class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine = list(magazine) 
        for ch in ransomNote:
            if ch in magazine:              
                magazine.remove(ch)             
                
            else:
                return False

        return True
