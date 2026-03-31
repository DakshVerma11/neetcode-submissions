class Solution:
    def simplifyPath(self, path: str) -> str:
        pathlist=path.split('/')
        print(pathlist)
        stack=[]
        
        for i in pathlist:
            if i==".":
                continue
            elif i=='..' and stack:
                stack.pop()
            elif i!='' and  i!='..' :
                stack.append(i)
            
        output=''
        if path[0]=='/':
            output='/'+'/'.join(stack)
        else:
            output='/'.join(stack)
        return output
            
        