class Solution:
    def armstrongNumber (self, n):
        # code here 
        in_string = str(n)
        sums = 0
        for i in in_string:
            sums += int(i)**3
        if sums == n:
            return "true"
        else:
            return "false"