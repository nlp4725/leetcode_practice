from typing import List

def warm_tem(tem_list:List[int])->List[int]:

    # check if empty
    if not tem_list:
        return []
    
    my_stack=[]
    i=0
    results={} # to remember i and their min warm temp's index

    for i,e in enumerate(tem_list):
        pair=(e,i) # a tuple to remember the index

        if not my_stack: # if stack is empty, add s[i] on top
            my_stack.append(pair)

        else: # if not, compare
            while tem_list[i] > my_stack[-1][0]: # if it is warmer and stack is not empty. 
                results[my_stack[-1][1]]=i # save top's index as key and warmer's index as value
                my_stack.pop()
                if not my_stack: # if nothing left after pop, we don't continue
                    break
            
            my_stack.append(pair) # till stack is empty or no longer warmer than previous, add to top
    warm_list=[]

    for i in range(len(tem_list)):
        if i in results:
            warm_list.append(results[i]-i)
        else:
            warm_list.append(0)
    return warm_list 


print(warm_tem([73,74,75,71,69,72,76,73]))