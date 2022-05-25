x = int(input())
num1 = list(map(int, input().split()))
a, b = map(int, input().split())
ans = x
for num in num1:
    num -= a
    if num < 0:
        continue
    ans += num // b if num % b == 0 else num // b + 1
print(ans)

