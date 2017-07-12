# create array
arr = np.arange(11,36)
arr.resize(5,5)

# Green
print(arr[::2, ::2])
print("-"*15)

# Blue
print(arr[1:4, 0])
print("-"*15)

# Red
print(arr[0, 1:4])
print("-"*15)

# Purple
print(arr[:, 1])
print("-"*15)
