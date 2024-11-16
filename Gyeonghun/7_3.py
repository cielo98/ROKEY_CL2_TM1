# 달리기 경주
# https://school.programmers.co.kr/learn/courses/30/lessons/178871

def solution(players:list, callings:list):
    positions = {runner : i for i, runner in enumerate(players)}

    for called in callings:
        idx = positions[called]
        if idx > 0:
            prev_player = players[idx - 1]
            players[idx], players[idx - 1] = players[idx - 1], players[idx]
            positions[called] -= 1
            positions[prev_player] += 1

    return players


# print(solution(["mumu", "soe", "poe", "kai", "mine"],
#                 ["kai", "kai", "mine", "mine"]))