def solution(n):
    answer = 0
    
    for i in range(2, n+1):
        check = 0
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                check = 1
                break
        
        if check != 1:
            answer += 1
                      
    return answer