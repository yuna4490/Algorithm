def solution(food):
    answer = ''
    
    for i in range(len(food)):
        if food[i] >= 2:
            answer += str(i) * (food[i]//2)
    
    answer += '0'
    
    for i in range(len(answer)-2, -1, -1):
        answer += answer[i]
        
    return answer