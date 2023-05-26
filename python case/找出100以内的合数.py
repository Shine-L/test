#合数是在大于1的整数中，除了能被1和本身整除外，也能被其他数整除的数
for i in range(2,101):
    for n in range(2,i):
        if i%n==0:
            print(i)
            break