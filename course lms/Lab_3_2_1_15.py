c0 = int(input("input the number: "))
step = 0

while c0 != 1:
    if c0 % 2 ==0:
        c0 = c0 / 2
    elif c0 % 2 ==1:
        c0 = 3 * c0 + 1
    print(int(c0))
    step +=1

print("step =", step)

