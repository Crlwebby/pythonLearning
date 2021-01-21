
sum = 0
#1-1000 sum
for i in range(1,1001):
# range(x,y) is equal to [x,y)
# range(x,y,z) is equal to x,x+z,x+2z,……
    sum += i
print(sum)

#sum for even number
sum = 0
for i in range(0,1001,2):
    sum +=i
print(sum)