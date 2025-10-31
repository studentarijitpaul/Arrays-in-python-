import ctypes

# Create C-style integer array with 5 elements
ArrayType = ctypes.c_int * 5
arr = ArrayType(10, 20, 30, 40, 50)

print("C array elements:")
for i in arr:
    print(i)

# Access individual element
print("Third element:", arr[2])

# Modify value
arr[1] = 99
print("After change:", [x for x in arr])
