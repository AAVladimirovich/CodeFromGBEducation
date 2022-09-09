# list1 = []
# for i in range(5):
#     print ('Enter number,' ,i, ': ')
#     x = float(input())
#     list1.append(x)
# number = max(list1)
# print('maximum value = ', number)

list2 = [1,33,44,123,551]
max = list2[0]
for i in list2:
    if i >= max:
        max = i

print ('maximum value = ' , max)