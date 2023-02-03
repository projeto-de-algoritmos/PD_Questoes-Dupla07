class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        a=[]
        
        def fun(a,s,f,l): 
            if f==0:
                if l==0:
                    a.append(s)
                    return
                while l!=0:
                    s+=")"
                    l+=-1
                a.append(s)
                return
            fun(a,s+"(",f-1,l) 
            if f!=l: 
                fun(a,s+")",f,l-1) 
            return

        fun(a,"",n,n) 
        return a 