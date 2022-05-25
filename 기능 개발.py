def solution(progresses, speeds):
    answer = []
    while progresses > 0:
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
        day = 0
        while progresses > 0:
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                day += 1
            else: break
        if day == True:
            answer.append(day)
    return answer