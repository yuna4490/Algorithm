def solution(players, callings):
    answer = []
    
    ranking = {player: int(idx) for idx, player in enumerate(players)}
    
    for calling in callings:
        current_rank = ranking[calling]
        ranking[calling] -= 1 # 추월한 선수 순위 변경
        
        ranking[players[current_rank-1]] += 1 # 추월당한 선수 순위 변경
        
        players[current_rank], players[current_rank-1] = players[current_rank-1], players[current_rank]
    
    
    return players

      
    # idx 사용으로 시간초과
    # for calling in callings:
    #     idx = players.index(calling)
    #     players[idx], players[idx-1] = players[idx-1], players[idx]
    
    
    # return players