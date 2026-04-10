from typing import List

def valid_parentheses(s: str)-> bool:
    if not s: # check if empty
        return False
    
    my_stack=[]
    my_dict={'(':')', '[':']','{':'}'}

    i=0

    for i in range(len(s)):
        if s[i] in my_dict:
            my_stack.append(s[i])
        elif s[i] not in my_dict and len(my_stack)==0:
            return False
        else:
            if s[i]==my_dict[my_stack[-1]]: # check if s[i] matches stack's top's pair
                my_stack.pop() # remove last element
            else:
                return False
    if len(my_stack)!=0:
        return False
    else:
        return True


print(valid_parentheses('()'))