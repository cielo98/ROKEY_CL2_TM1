# 광물 캐기
# https://school.programmers.co.kr/learn/courses/30/lessons/172927

def solution(picks, minerals):
    answer = 0
    fatigue = 0
    mineral_list = []
    temp = [minerals[i:i+5] for i in range(0, len(minerals), 5)]

    for list_ in temp:
        count_dia = list_.count("diamond")
        count_iron = list_.count("iron")
        count_stone = list_.count("stone")
        mineral_list.append([count_dia, count_iron, count_stone])
    if len(mineral_list) > sum(picks):
        mineral_list = mineral_list[:sum(picks)]
    sorted_list = sorted(mineral_list, key=lambda x: (x[0], x[1], x[2]))
    # print(sorted_list)
    
    for idx, num in enumerate(picks):
        if idx == 0:
            for i in range(num):
                if not sorted_list:
                    break
                dig = sorted_list.pop()
                fatigue += sum(dig)
            
        elif idx == 1:
            temp = 0
            for i in range(num):
                if not sorted_list:
                    break
                dig = sorted_list.pop()
                fatigue += 5*dig[0] + 1*dig[1] + 1*dig[2]
                
        else:
            temp = 0
            for i in range(num):
                if not sorted_list:
                    break
                dig = sorted_list.pop()
                fatigue += 25*dig[0] + 5*dig[1] + 1*dig[2]
                
    return fatigue

# print(solution(
#     [0, 0, 1], 
#     ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
# ))