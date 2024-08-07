class Solution:
    def lcmAndGcd(self, A , B):
        def GCD(a,b):
            while a>0 and b>0:
                if a>b: a%=b
                else:b%=a
            if a==0:return b
            return a
        gcd=GCD(A,B)
        lcm=(A*B)//gcd
        return lcm,gcd