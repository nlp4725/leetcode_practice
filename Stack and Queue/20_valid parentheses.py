def valid_p(s:str)->bool:
    i = 0 # initiate a pointer
    myStack=[] 
    brackets={'(':')','{':'}','[':']'} # a dictionary to store open:closed brackets pair

    while i <=len(s)-1:
        if not myStack: # if mystack is empty, we add s[i] to stack
            myStack.append(s[i])

        else: # if not empty, check if it is a open or close brackets
            if s[i] in brackets: # it is a open bracket
                 myStack.append(s[i])
            else: # for closed, if we check if it matches stack's top
                if s[i]==brackets[myStack[-1]]:
                    myStack.pop()
                else:
                    return False
        # move pointer for append cases
        i+=1

    return len(myStack)==0 # if stack is empty then it is valid

print(valid_p('()[]{}'))
print(valid_p('([][]{}'))
