class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        stack.append(int(operations[0]))
        for i in range(1,len(operations)):
            if operations[i]=='D':
                newres=2*int(stack[-1])
                stack.append(newres)
            elif operations[i]=='+':
                new=stack[-1]+stack[-2]
                stack.append(new)
            elif operations[i]=='C':
                n=operations[i-1]
                stack.pop()
            else:
                stack.append(int(operations[i]))
        return sum(stack)


        