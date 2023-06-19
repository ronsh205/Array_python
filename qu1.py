import array as arr

# define array integer
# i it integer and d is double type flag
arr1 = arr.array('i', [1, 8, 95, 6, 5, 9])
# remove vaule location 1
# arr1.pop(1)
arrtemp = arr1[0:3]

for i in arrtemp:
    print(i)
