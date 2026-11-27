# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right


# from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        result = []
        queue = deque([root]) # print(queue) give deque root address. think of this as a list of addresses. pointers. 

        while queue:  
            level = []
            for _ in range(len(queue)): # number of times we pop it off 
                node = queue.popleft()
                level.append(node.val)
                
                if node.left: 
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)
        
        return result 
















#         if not root: # if root i empty, return an empty list
#             return []

#         queue = deque([root]). # we initiaze a deque with the root (think of this as a doubly linked list, bidrection)
#         result = [] # intialize the array that we will store our values in 

#         while queue: # loop through queue
#             level = [] # create a level, it acts as a flag? 

#             for _ in range(len(queue)): # loop through the size of the queue
#             # im guessing termination happens when length of queue is 0
#                 node = queue.popleft() # left side of array is the first-in list, newest (latest) element is on the right. first set the root as node, then pop it off the queue. 
#                 level.append(node.val) # the question to ask is i am thinking node as a value apparement not. node is another pointer, is a treenode data type. value of node is 1. 

#                 if node.left:
#                     queue.append(node.left) # we have done somthing using the root, now we go to left neighbours

#                 if node.right:
#                     queue.append(node.right)

#             result.append(level)

#         return result

# create a queue with the root (first in element), store node (we use this to do operations), pop it off. append the queue with the left and right neighbours. [2 3]

# # solve this question (copy and paste is fine) but think!
# # rewrite bfs algorithmn

# queue
# example: Input: root = [1,2,3,4,5,6,7]
# this case: 
# loop len: 1
# [1] -> results [1]
# []
# [2 3] loop len: 2
# results [2]
# [3 4 5]
# results [2 3]
# [4 5 6 7] loop len: 4
# [5 6 7]
# [6 7]
# [7]
# [] loop len 0 exit loop 

# normal bfs
# [1]
# []
# [2 3] 
# [3 4 5]
# [4 5 6 7]
# [5 6 7]
# [6 7]
# [7]
# []
# terminal