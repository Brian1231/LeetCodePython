class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1:
            return True
        else:
            capCount = 0
            firstIsCap = False
            atStart = True
            for char in word:
                if char.isupper() and atStart:
                    capCount += 1
                    atStart = False
                    firstIsCap = True
                elif char.isupper():
                    atStart = False
                    capCount += 1
                else:
                    atStart = False

            return (capCount == 0) or (capCount == 1 and firstIsCap) or (capCount == len(word))

