def pop_duplicates(s:str)->str:
    i = 0
    myStack=[]

    while i<=len(s)-1:
        if not myStack: # if empty, add to the stack and move the pointer
            myStack.append(s[i])
        else: # if not empty, compare
            if s[i] == myStack[-1]: # if next char in s matches stack's top,pop
                myStack.pop()
            else: # else add current char to stack
                myStack.append(s[i])
        i+= 1

    return str(''.join(myStack))

print(pop_duplicates('abbaca'))

