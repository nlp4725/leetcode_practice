from typing import List
def check(nums:List[str])->int:

    # check empty
    if not nums:
        return 0
    
    my_stack=[]

    for num in nums:
        # if digit, append
        is_num=False

        try:
            int(num)
            is_num=True
            my_stack.append(int(num))
        except ValueError:
            pass

        if not is_num:
            if num=="+":
                my_stack.append(int(my_stack.pop())+int(my_stack.pop()))
            elif num=='-':
                a,b=int(my_stack.pop()),int(my_stack.pop())
                my_stack.append(b-a)

            elif num=="*":
                my_stack.append(int(my_stack.pop())*int(my_stack.pop()))

            else:
                a,b=int(my_stack.pop()),int(my_stack.pop())
                my_stack.append(int(b/a))
    return my_stack[0]

        
print(check( ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print(check( ["4","13","5","/","+"]))