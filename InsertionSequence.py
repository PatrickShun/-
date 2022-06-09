# 插入式序列
# 首先最左端的值已完成排序，然后将第二个开始的数值执行对比，如果比第二个数值比第一个数值小，则交换位置，移动后再次对比前面的值，一直重复；

l1 = [2,3,6,4,5,8,9,1,7]
count = 0
for i in range(1,9):
    # print(l1[i])
    for k in range(len(l1)):
        if l1[i] <= l1[k]:
            print("换")
            l1[i],l1[k] = l1[k],l1[i]
            print(l1,"\n")
            count += 1
        else:
            print("PASS")
            print(l1,"\n")

    print("=" * 30)

print(l1)
print(count)