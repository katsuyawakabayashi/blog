class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")": "(", "}": "{", "]": "["}
        stack = []
        
        for i in s:
            if i in dic.values():
                stack.append(i)
            elif stack and stack[-1] == dic[i]:
                stack.pop()
            else:
                return False
        return stack == []
                
