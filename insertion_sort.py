nums = [33, 47, 98, 12, 14, 58, 61, 9, 87, 73]


def insertion_sort(nums):

   for i in range(1,len(nums)):

     current_num = nums[i]
     position = i

     while position > 0 and nums[position-1] > current_num:
         nums[position] = nums[position-1]
         position = position-1

     nums[position] = current_num

insertion_sort(nums)
print(nums)
