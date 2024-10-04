print("1. implementasi bubble sort")
array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(array)
for i in range(n-1):
    for j in range(n-i-1):
        if array[j] > array[j+1]:
             array[j], array[j+1] = array[j+1], array[j]
print(array)

print(f"\n 2. implementasi bubble sort menggunakan fungsi")
def bubble_sort(arr):
  for i in range(len(arr)-1, 0, -1):
    for j in range(i):
      if arr[j] > arr[j+1]:
          arr[j], arr[j+1] = arr[j+1], arr[j]
          
arr = [39, 12, 18, 85, 72, 10, 2,18]
print("data tidak diurutkan")
print(arr)

bubble_sort(arr)
print("data diurutkan")
print(arr)

print(f"\n 3. implementasi selection sort")
array1 = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(array1)
for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if array1[j] < array1[min_index]:
            min_index = j 
    min_value = array1.pop(min_index)
    array1.insert(i, min_value)
print(array1)

