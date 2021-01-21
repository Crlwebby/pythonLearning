for i in range(1,10000):
    sum = 0
    for j in range(1,int(i ** 0.5) + 1):
        if i%j == 0:
            sum +=j
            if j > 1 and i != j * j:
                sum += i // j
    if sum == i:
        print(sum)