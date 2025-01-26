
import numpy as np

arr = np.array([1, 2, 2, 3, 6, 4])
print(arr)
arr = np.arange(1,7)
print(arr)
arr = np.zeros(3)
print(arr)
arr = np.ones(3)

print(arr)

arr = [1, 2, 3, 4, 5, 6]
print("The square of the each value of the arr is: ", np.square(arr))


print(np.random.rand(5))


print(np.random.randint(1,10,5))

arr = np.array([1, 2, 3, 4, 5, 6])
maxi = np.max(arr)
print(maxi)
print(np.min(arr))

print(arr)


arr = np.array([[1, 2, 3],[6, 5, 4]], np.int32)
print(type(arr))
print(arr.shape)
print(arr.dtype)

print(arr)
