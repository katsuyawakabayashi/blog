class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        strx = str(x)
        if len(strx) == 1: return True
        if len(strx) == 2: return True if strx[0] == strx[1] else False 
        l, r = 0, len(strx) -1
                
        while l < r:
            if strx[l] != strx[r]:
                return False
            l += 1
            r -= 1
            if l == r or l+1 == r:
                if strx[l] == strx[r]:
                    return True
