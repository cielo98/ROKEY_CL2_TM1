# 숫자 짝꿍
# https://school.programmers.co.kr/learn/courses/30/lessons/131128

def solution(X, Y):
    x, y = {}, {}
    answer = ''
    
    for i in X:
        if i in x:
            x[i] += 1
        else:
            x[i] = 1
    
    for j in Y:
        if j in y:
            y[j] += 1
        else:
            y[j] = 1
    
    keys = sorted(x.keys(), reverse=True)
    
    for num in keys:
        if num in y.keys():
            m = min(x[num], y[num])            
            answer += num*m
    
    if answer == '':
        answer = '-1'
    if answer[0] == '0':
        answer = '0'
        
    return answer

# print(solution("100", "2345"))
# print(solution("100", "203045"))
# print(solution("100", "123450"))
# print(solution("12321", "42531"))
# print(solution("5525", "1255"))