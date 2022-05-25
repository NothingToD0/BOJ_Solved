triangle = [10,24,26]

def is_angle(a_list):
    if(sum(a_list)!=180): return "삼각형이 아니다"
    elif(len(a_list)!=3): return "삼각형이 아니다"
    else:
        if(max(a_list) > 90): return "둔각삼각형"
        elif(max(a_list) == 90): return "직각삼각형"
        else: return "예각삼각형"

print(is_angle(triangle))

