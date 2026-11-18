class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1 

        while left < right: # terminates when left == right
            if numbers[left] + numbers[right] == target: 
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -=1

            



# input properties: 
# - sorted (smallest at left, largest at right)
# - if we add leftmost and rightmost, and its too large, it means we need to reduce. the only way is to move the right pointer to left since this is sorted
# - if too small, we move left pointer rightward to increase (sorted, remember)
# - terminate when pointer meets 

# what is the brute force approach? 

# what info can i exploit?

# can i eliminate revisiting the elements 
        