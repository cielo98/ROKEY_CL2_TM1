# 신고 결과 받기
#  https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = {name: 0 for name in id_list}
    report_count = {name: 0 for name in id_list}
    id = {name: set() for name in id_list}
    
    for a in report:
        user, reported_person = a.split()
        if user != reported_person and user not in id[reported_person]:
            id[reported_person].add(user)
            report_count[reported_person] += 1
    
    for key, value in report_count.items():
        if value >= k:
            for person in id[key]:
                answer[person] += 1
    
    # print(report_count)
    # print(id)
        
    return list(answer.values())


print(solution(
    ["muzi", "frodo", "apeach", "neo"],
    ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
    2
))

# print(solution(
#     ["con", "ryan"],
#     ["ryan con", "ryan con", "ryan con", "ryan con"], 3
# ))