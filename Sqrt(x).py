#Sqrt(x) x的平方根

'''
本题有多种解法，以下列写二分法与牛顿迭代法程序：
二分法：将待开方的数视为终点，以mid**2 > or <x为判别条件
这里要特别注意由于结果是向下取整，因此当x/mid<mid的场合，不应该将mid传递给ans
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        mid=0
        start=0
        end=x
        if x==0:
            ans=0
        elif x==1:
            ans=1
        else:
            while(start<=end):
                mid=start+(end-start)//2
                if x/mid<mid:  #这样写是为了避免内存溢出
                    end=mid-1
                elif x/mid>mid:
                    start=mid+1
                    ans=mid
                else:
                    ans=mid
                    break
        return ans

'''
牛顿法：y=x^2-C   其中C为待开方的数，故该问题可转换为求函数与x轴交点的问题。
取X0为C，计算y值，以该点做斜率为2x0的切线，列切线方程，求其与x轴交点；
令该交点为x1；重复迭代。。。
以abs(xi+1-xi)设置某一终止值为结束条件,小于该条件说明误差已经缩小到足够小。
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        C, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + C / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi
        
        return int(x0)  #返回值记得取整呀

