# 最小的k个数
# 方法一：使用堆
# 思路：我们用一个大根堆实时维护数组的前k小值。首先将前k个数插入到大根堆中，随后从第k+1个数开始遍历数组，如果当前遍历
# 的数比大根堆堆顶的值小，我们将堆顶的值弹出，将当前遍历的数插入堆顶。最后将弹出的堆顶值存入数组返回即可。注意：
# Python语言中只有小根堆，因此我们要对数组中所有的数取其相反数，才能使用小根堆维护前 k 小值。
class Solution:
    def getLeastNumbers(self,arr: List[int],k: int) -> List[int]:
        if k == 0:
            return list()
        hp = [-x for x in arr[:k]] # 构建前k个数的大根堆
        heapq.heapify(hp) # 堆化
        for i in range(k,len(hp)): # 从第k+1个数开始遍历数组
            if -hp[0] > arr[i]: # 如果堆顶的值大于当前遍历的值
                heapq.heappop(hp) # 弹出堆顶的值
                heapq.heappush(hp,-arr[i]) # 将当前遍历的值存入堆顶
        ans = [-x for x in hp] # 将弹出的堆顶值存入数组
        return ans
