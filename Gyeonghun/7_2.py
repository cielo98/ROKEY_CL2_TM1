# 방금그곡
# https://school.programmers.co.kr/learn/courses/30/lessons/17683

def solution(m, musicinfos):
    melody = []
    new_m = ''
    for alphabet in m:
        if alphabet == '#':
            new_m = new_m[:-1] + new_m[-1].lower()
        else:
            new_m += alphabet    
    
    for infos in musicinfos:
        info = infos.split(",")
        # print(info)
        t = ''
        for alphabet in info[3]:
            if alphabet == '#':
                t = t[:-1] + t[-1].lower()
            else:
                t += alphabet  
        info[3] = t
        
        start_time = int(info[0][:2]) * 60 + int(info[0][-2:])
        end_time = int(info[1][:2]) * 60 + int(info[1][-2:])
        play_time = end_time - start_time
        
        song = info[3]
        song_time = len(song)
        song_q = play_time // song_time
        song_r = play_time % song_time
        
        melody.append([info[2], play_time, song*song_q + song[:song_r]])
    sort_melody = sorted(melody, key=lambda x:x[1], reverse=True)
    # print(melody)
    for l in sort_melody:
        if new_m in l[2]:
            return l[0]
        
    return '(None)'

print(solution("ABCDEFG", 
               ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", 
               ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", 
               ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))