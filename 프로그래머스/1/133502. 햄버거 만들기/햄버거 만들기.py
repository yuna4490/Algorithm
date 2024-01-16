def solution(ingredient):
    answer = 0
    burger = []
    
    # 2 : 야채, 1 : 빵, 3 : 고기
    # 1 2 3 1
    
    for i in ingredient:
        burger.append(i)
        
        if burger[-4:] == [1,2,3,1]:
            answer += 1
            
            for i in range(4):
                burger.pop()
        
    return answer