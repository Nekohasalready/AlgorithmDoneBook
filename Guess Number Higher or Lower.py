#Guess Number Higher or Lower 猜数字大小

'''
猜数字大小：
对手已经作为函数给我们了，只要调用然后比较就可以，很简单
'''

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start=1
        end=n
        if n==1:
            return 1
        else:
            while(start<=end):
                mid=start+(end-start)//2
                backnum=guess(mid)
                if backnum==-1:  
                    end=mid-1
                elif backnum==1:
                    start=mid+1    
                else:
                    return mid
                    
                

    
