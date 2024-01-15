def solution(k, m, score):
    answer = 0
    
    score = sorted(score, reverse = True)
    
    length = len(score) // m
    
    i = 0
    for _ in range(length):
        s = min(score[i:i+m])
        i += m
        answer += s * m
        
    return answer