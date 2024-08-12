class Solution:
    def reverseEqn(self, s):
        operator = ["+","-","*","/"]
        temp = ""
        stack = []
        for i in s:
            if i in operator:
               stack.append(temp)
               temp = ""
               stack.append(i)
            else:
                temp = temp + i
        stack.append(temp)
        res = "".join(stack[::-1])
        return res
            