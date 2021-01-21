#用筛法找素数，以空间换时间

array = []
for i in range(0,1001):
    array.append(1)

for i in range(2,1001):
    if array[i] == 1:
        for j in range(2, 1000//i + 1):
            array[i * j] = 0

count = 0
for i in range(2,1001):
    if array[i] == 1:
        count += 1
        print(i)

print(count)