num = int(input())
sum = 0
j = 0
for i in range(1 , num + 1):
    sum += i

result = ' + '.join(str(i) for i in range(1, num + 1)) + ' = ' + str(sum)
print(result)