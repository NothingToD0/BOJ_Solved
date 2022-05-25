def solution(number, k):
    배열 = []
    for (i, num) in enumerate(number):
        while 배열 and 배열[-1] < num and k > 0:
            배열.pop()
            k -= 1
        if k == 0:
            배열 += number[i:]
            break
        배열.append(num)
    배열 = 배열[:-k] if k > 0 else 배열
    answer = "".join(배열)
    return answer