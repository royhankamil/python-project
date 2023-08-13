array1 = [[30, 60, 7], [19, 32,5], [15, 52, 64]]
array2 =[[25, 68, 5], [11, 86, 35], [31, 74, 3]]
for c in array1:
    print(c)
print('\n')
for f in array2:
    print(f)
print('\n')
for i in range(3):
    for e in range(3):
         total = array1[i][e] + array2[i][e]
         print('array range [' + str(i) + '] saling bertambah = ' + str(total))