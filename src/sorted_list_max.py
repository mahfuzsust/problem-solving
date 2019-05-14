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

if __name__ == '__main__':
    A = [5, 6, 7, 9, 11, 345, 567, 1, 3]
    print(get_largest_item(A))
