def find(s,x):
    if x not in s:
        return -1
    else:
        for i in range(0,len(s)):
            if(s[i:i+len(x)]==x):
                return i
def rfind(s,x):
    if x not in s:
        return -1
    else:
        ans=-1
        for i,j in enumerate(s):
            if(s[i:i+len(x)]==x):
                ans=i
        return ans
def count(s,x):
    c=0
    for i,j in enumerate(s):
        if s[i:i+len(x)]==x:
            c+=1
    return c
def first(s):
    return s.split()[0]
