# 选择性排序，线性搜索序列，找到最小值，并移动到第一位；


l1 = [2,3,6,4,5,8,9,1,7]

# print(len(l1))
for i in range(len(l1)):
    key1 = l1[i]
    for j in range(len(l1)):
        key2 = l1[j]
        if key1 >= key2:
            print("PASS")
        else:
            print("移动")
            l1[i],l1[j] = l1[j],l1[i]
    print("="*30)


print(l1)


