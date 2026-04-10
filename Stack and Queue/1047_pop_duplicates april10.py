def pop(s:str)->str:
    if not s:
        return ''
    
    my_stack=[]
    i=0
    
    for i in range(len(s)):
        if len(my_stack)==0:
            my_stack.append(s[i])

        else:
            if s[i]==my_stack[-1]:
                my_stack.pop()
            else:
                my_stack.append(s[i])
    
    return ''.join(my_stack)

print(pop('abbaca'))
