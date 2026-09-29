class Solution:
    def checkValidString(self, s: str) -> bool:
        openIndicies, starIndicies = [], []

        for i, ch in enumerate(s):
            if ch == '(':
                openIndicies.append(i)
            elif ch == '*':
                starIndicies.append(i)
            else:
                if not len(openIndicies) and not len(starIndicies):
                    return False
                if openIndicies:
                    openIndicies.pop()
                elif starIndicies:
                    starIndicies.pop()
        
        while openIndicies and starIndicies:
            openIdx, starIdx = openIndicies.pop(), starIndicies.pop()
            if openIdx > starIdx:
                return False
            
        return not len(openIndicies)
                