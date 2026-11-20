class Solution:
    # Approach 1: prefix/suffix max arrays. O(n) time, O(n) space.
    # def trap_prefix(self, height: List[int]) -> int:
    #     n = len(height)
    #     if n == 0:
    #         return 0

    #     maxLeft = [0] * n
    #     maxLeft[0] = height[0]
    #     for i in range(1, n):
    #         maxLeft[i] = max(maxLeft[i - 1], height[i])

    #     maxRight = [0] * n
    #     maxRight[n - 1] = height[n - 1]
    #     for i in range(n - 2, -1, -1):
    #         maxRight[i] = max(maxRight[i + 1], height[i])

    #     total = 0
    #     for i in range(n):
    #         total += min(maxLeft[i], maxRight[i]) - height[i]
    #     return total

    # Approach 2: two pointers. O(n) time, O(1) space. This is the optimal one.
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxLeft, maxRight = 0, 0
        total = 0

        while l < r:
            if height[l] < height[r]:
                # right side has a wall at least this tall,
                # so the left side is the limiting wall
                maxLeft = max(maxLeft, height[l])
                total += maxLeft - height[l]
                l += 1
            else:
                # left side has a wall at least this tall,
                # so the right side is the limiting wall
                maxRight = max(maxRight, height[r])
                total += maxRight - height[r]
                r -= 1

        return total