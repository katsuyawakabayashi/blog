class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        charSet = set()
        
        for c in s:
            charSet.add(c) if c not in charSet else charSet.remove(c)
      
        return len(charSet) <= 1
                
