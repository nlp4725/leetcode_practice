from typing import List

def searchMatrix(nums:List[List[int]],target:int)->bool:
    if not nums: # check if empty
        return False
    
    m=len(nums)# rows
    n=len(nums[0]) # columns
    
    left=0
    right=m*n-1

    while left<=right: # because we move pointers to mid+1 or mid-1, we can use =
        mid=left+(right-left)//2

        # convert mid to 2-d index
        rows=mid//n
        cols=mid%n
        result=nums[rows][cols]
        # compare to target
        if result==target:
            return True
        elif result<target: # need to search right
            left=mid+1
        else:
            right=mid-1
    
    return False




print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 100))