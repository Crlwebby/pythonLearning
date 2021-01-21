one_place = 0
tens_place = 0
hundreds_place = 0

for i in range(100,1000):
    hundreds_place = i // 100
    tens_place = (i % 100 ) // 10
    one_place = i % 10;
    if hundreds_place ** 3 + tens_place ** 3 + one_place ** 3 == i:
        print(i)