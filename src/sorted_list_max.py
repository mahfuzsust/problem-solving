def get_largest_item(arr):
   if(arr == None or not isinstance(arr, list) or len(arr) == 0):
       return None
   first = arr[0]
   last = arr[-1]

   if(len(arr) == 1):
       return first
   if(first < last):
       return last
   mid = len(arr)//2
   return max(get_largest_item(arr[:mid]), get_largest_item(arr[mid:]))
