#Search in Rotated Sorted Array 搜索旋转排序矩阵

'''
中等难度的题，但是其实如果if-else补丁打的足够的话，还是能在二分法的原语句上写出来。
我一开始就删删改改写了很长一段程序，提交通过了。但是很明显这种方式非常的不整洁，所以又参考了标准的方法进行了重构。

以测试用例[4,5,6,7,0,1,2] 为例：
无论如何切分，至少有一半的搜索范围是有序的，我们将利用这一规律构建我们的搜索程序。

首先初始化start和end位置，然后根据end判断数组是不是只有1个值，如果是的话直接和目标值比较，返回检测结果；
如果数组有多个值，则进行循环：
1.更新mid位置；
2.判断nums[mid]是否等于目标值，如果是则返回Mid,如果不是则继续循环；
3.判断左侧是否为有序区间（用小于等于号，因为可能此时start和mid已经重合），如果是则继续判断目标值是否位于区间内，如果不是则判断目标值在另一区间中；
4.如果步骤3的初始条件不成立，则判断右侧为有序区间，其余步骤同上;
5.如果全部搜索未得到结果，则return -1.

这道题要注意的重点除了对有序区间的判断以外，还要注意里面涉及了区间头和区间尾的比较，这在前面的简单算法题中都是没有出现过的，这时候需要我们考虑到区间为1的情况，
如果还使用<或者>，那么程序的运行会发生错误。

'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1

        if end==0:
            if nums[0]==target:
                return 0
            else:
                return -1
        else:
            while(start<=end):
                mid=start+(end-start)//2
                if nums[mid]==target:
                    return mid
                elif nums[start]<=nums[mid]:  #左边是有序区间，注意这里用到的都是<=和>=，这是本题与其它题目的最大区别
                    if nums[start]<=target<=nums[mid]:
                        end=mid-1
                    else:
                        start=mid+1
                elif nums[mid]<=nums[end]:
                    if nums[mid]<=target<=nums[end]:
                        start=mid+1
                    else:
                        end=mid-1
            return -1


                    
