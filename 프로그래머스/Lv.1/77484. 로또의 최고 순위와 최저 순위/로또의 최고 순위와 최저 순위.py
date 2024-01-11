def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt = 0
    
    for lotto in lottos:
        for num in win_nums:
            if lotto == num:
                cnt += 1
    
    x = lottos.count(0)
    
    answer = [rank[cnt+x], rank[cnt]]
    
    return answer