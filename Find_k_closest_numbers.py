class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        由于要返回的数域长度是固定的，所以我们只要关注数组左侧起点的搜索范围即可，知道了左侧起点即可根据k得右侧终点
        '''
        size = len(arr)
        left = 0
        right = size - k #限制左侧边界最大值

        while left < right: #因为限制了left<right作为条件，所以在下面可以使用arr[mid+k]
            mid = left + (right - left) // 2
            # 尝试从长度为 k + 1 的连续子区间删除一个元素
            # 从而定位左区间端点的边界值
            if x - arr[mid] > arr[mid + k] - x: #该条件对应两种情况：1.x在区间中，但更偏向mid+k那一边；2.x在区间外，且在mid+k右侧
                left = mid + 1   #我们把搜索范围的左极限往右移动1格，不能移动的太多，不然可能就错过了
            else:  #这里对应另两种情况：1.x在区间中，但更偏向mid那一边；2.x在区间外，且在mid左侧
                right = mid  #这样我们把左侧起点的搜索右极限顶到Mid位置，注意：由于其更偏向mid，x依然在k域内
        return arr[left:left + k]
