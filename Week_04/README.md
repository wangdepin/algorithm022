# 第四周学习笔记

## 深度优先搜索和广度优先搜索算法

1. DFS 代码模板：

   + 递归写法：

     ```python
     #Python
     visited = set() 
     
     def dfs(node, visited):
         if node in visited: # terminator
         	# already visited 
         	return 
     
     	visited.add(node) 
     
     	# process current node here. 
     	...
     	for next_node in node.children(): 
     		if next_node not in visited: 
     			dfs(next_node, visited)
     ```

   - 非递归写法：

     ```python
     #Python
     def DFS(self, tree): 
     
     	if tree.root is None: 
     		return [] 
     
     	visited, stack = [], [tree.root]
     
     	while stack: 
     		node = stack.pop() 
     		visited.add(node)
     
     		process (node) 
     		nodes = generate_related_nodes(node) 
     		stack.push(nodes) 
     
     	# other processing work 
     	...
     ```

2. BFS 代码模板

   ```python
   # Python
   def BFS(graph, start, end):
       visited = set()
   	queue = [] 
   	queue.append([start]) 
   	while queue: 
   		node = queue.pop() 
   		visited.add(node)
   		process(node) 
   		nodes = generate_related_nodes(node) 
   		queue.push(nodes)
   	# other processing work 
   	...
   ```

   

## 贪心算法

贪心算法是一种在每一步选择中都采取在当前状态下最好或最优（即最有利）的选择，从而希望导致结果是全局最好或最优的算法。

贪心算法与动态规划的不同在于它对每个子问题的解决方案都做出选择，不能回退。动态规划则会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。

具体解决的问题：

+ 贪心法可以解决一些最优化问题，如：求图中的最小生成树、求哈夫曼编码等。然而对于工程和生活中的题，贪心法一般不能得到我们所要求的答案。
+ 一旦一个问题可以通过贪心法来解决，那么贪心法一般是解决这个问题的最 好办法。由于贪心法的高效性以及其所求得的答案比较接近最优结果，贪心法也可以用作辅助算法或者直接解决一些要求结果不特别精确的问题。

## 二分查找(Binary Search)

- 二分查找是一种针对有序数据集合的查找算法，也叫折半查找算法。二分查找的思想非常简单，但是看似越简单的东西往往越难掌握好，想要灵活运用就更加困难。

  - 二分查找找针对的是一个有序的数据集合，查找思想有点类似分治思想。每次都通过跟区间的中间元素对比，将待查找的区间缩小为之前的一半，直到找到要查找的元素，或者区间被缩小为0。
  - O(logn) 惊人的查找速度
  - O(logn) 这种对数时间复杂度。这是一种极其高效的时间复杂度，有的时候甚至比时间复杂度是常量级 O(1) 的算法还要高效。为什么这么说呢？
  - 因为 logn 是一个非常“恐怖”的数量级，即便 n 非常非常大，对应的 logn 也很小。比如 n 等于 2 的 32 次方，这个数很大了吧？大约是 42 亿。也就是说，如果我们在 42 亿个数据中用二分查找一个数据，最多需要比较 32 次。

- 二分查找的递归与非递归实现

  - 非递归实现（最简单的情况就是有序数组中不存在重复元素）

  ```python
  # Python 代码模板
  left, right = 0, len(array) - 1 
  while left <= right: 
  	  mid = (left + right) / 2 
  	  if array[mid] == target: 
  		    # find the target!! 
  		    break or return result 
  	  elif array[mid] < target: 
  		    left = mid + 1 
  	  else: 
  		    right = mid - 1
  ```

  - 二分查找除了用循环来实现，还可以用递归来实现

  ```java
  
  // 二分查找的递归实现
  public int bsearch(int[] a, int n, int val) {
    return bsearchInternally(a, 0, n - 1, val);
  }
  
  private int bsearchInternally(int[] a, int low, int high, int value) {
    if (low > high) return -1;
  
    int mid =  low + ((high - low) >> 1);
    if (a[mid] == value) {
      return mid;
    } else if (a[mid] < value) {
      return bsearchInternally(a, mid+1, high, value);
    } else {
      return bsearchInternally(a, low, mid-1, value);
    }
  }
  ```

  二分查找应用场景的局限性：

  1. 首先，二分查找依赖的是顺序表结构，简单点说就是数组。

     - 那二分查找能否依赖其他数据结构呢？比如链表。答案是不可以的，主要原因是二分查找算法需要按照下标随机访问元素。我们在数组和链表那两节讲过，数组按照下标随机访问数据的时间复杂度是 O(1)，而链表随机访问的时间复杂度是 O(n)。所以，如果数据使用链表存储，二分查找的时间复杂就会变得很高。

  2. 其次二分查找针对的是有序数据

  3. 再次，数据量太小不适合二分查找

  4. 最后，数据量太大也不适合二分查找

- 二分查找的变形：

  ![image-20210111231325876](C:/Users/ThinkPad/AppData/Roaming/Typora/typora-user-images/image-20210111231325876.png)

     

     

     

     
  
     





