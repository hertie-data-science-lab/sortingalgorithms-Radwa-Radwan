from bucket import bucketSort
import time

data = [25, 67, 20, 4, 8]

start_time = time.time()
sorted_array = bucketSort(data)
end_time = time.time()

print(sorted_array)

execution_time = end_time - start_time
print(f"Execution_time: {execution_time} seconds")



