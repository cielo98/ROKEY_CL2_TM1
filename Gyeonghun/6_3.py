# 바탕화면 정리
# https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    x = []
    y = []
    lux, luy = 0, 0
    rdx, rdy = 0, 0
    
    row = len(wallpaper)
    col = len(wallpaper[0])
    
    for i in range(row):
        for j in range(col):
            if wallpaper[i][j] == '#':
                x.append(i)
                y.append(j)
    
    return [min(x), min(y), max(x)+1, max(y)+1]