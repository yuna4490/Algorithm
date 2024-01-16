def solution(ingredient):
    answer = 0
    stack = []
    
    # 2 : 야채, 1 : 빵, 3 : 고기
    # 1 2 3 1
    
    for i in ingredient:
        if not stack:
            if i == 1:
                stack.append(i)
        
        else:
            if i == 1:
                if stack[-1] == 3: 
                    stack = stack[0:len(stack)-3]
                    answer += 1
                
                else:
                    stack.append(i)
        
            elif stack[-1] == i-1:
                stack.append(i)
            
            else:
                stack = [] 
    
        # print(i, stack)
        
    return answer