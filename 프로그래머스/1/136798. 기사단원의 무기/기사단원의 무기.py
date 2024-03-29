def solution(number, limit, power):
    answer = 0
    
    for i in range(1, number + 1):
        cnt = 0 # 약수 개수
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                cnt += 1
                if j != i // j:
                    cnt += 1
                    
        if cnt > limit:
            answer += power
        
        else:
            answer += cnt
            
    return answer