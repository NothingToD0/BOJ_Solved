
number = 1924
val = []
k = 2
for i in str(number):
    val.append(i)
len = len(val)
print(len)
val.sort()
val.reverse()
print(val)
answer = 0
for o in range(k):
    val.pop()
val = list(map(int, val))
answer = int("".join([str(x) for x in val]))
print(answer)
