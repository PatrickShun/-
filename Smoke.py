# smoking algorithm
# 冒泡序列
# 在一个序列中对比最后两个的数值，对比后把小的移动到前面，否则不动，运行多次后可把序列按顺序排好

l1 = [8,9,5,6,4,3,1,2,7]

for n in range(8):
    for i in range(len(l1)-1):
        j = len(l1) - (i+1)
        k = j - 1

        print(l1[j],l1[k])
        if l1[k] < l1[j]:
            print("PASS")
        else:
            l1[j],l1[k] = l1[k],l1[j]
            print("换")

print(l1)


# print(l1[9-1])