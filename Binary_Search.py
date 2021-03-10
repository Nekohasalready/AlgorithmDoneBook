#Binary Search 二分查找
#执行用时：36 ms, 在所有 Python3 提交中击败了99.91% 的用户
#内存消耗：15.7 MB, 在所有 Python3 提交中击败了85.86% 的用户

'''
普通的二分查找是在已经从小到大排序的数组中进行查找。因此只要设置好范围起点和终点，以起点<=终点为循环条件，
根据起点与终点计算中点位置，比较目标值与中点值的大小。
如果目标值<中点值，则下一次搜索左边域；如果目标值>中点值，则下一次搜索右边域。
在此过程中，如果搜索到则return mid；如果一直到最后也搜索不到则返回-1

'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        listlenth=len(nums)
        
        '''定义二分范围的起点和终点'''
        start=0
        end=listlenth-1
        targetindex=-1 #如果最后没有找到目标值，那么返回-1
        
        '''开始循环，直到左边界>右边界为止'''
        while(start<=end):
            midindex=start+int((end-start)/2) #计算中点位置
            if nums[midindex]<target: #当前值比目标值小，那么应该在右侧继续搜寻
                start=midindex+1
            elif nums[midindex]>target: #当前值比目标值大，那么应该在左侧继续搜寻
                end=midindex-1
            else:
                targetindex=midindex #找到目标值，返回其位置
                break
        return targetindex
      
      
