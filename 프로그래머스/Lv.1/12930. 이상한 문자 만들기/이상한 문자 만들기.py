def solution(s):
    answer = ''
    
    s = list(s.split(" ")) # 공백이 한번이 아니라 여러번일 수 있기 때문에..... split() 으로 하면 틀린다
    
    for i in s:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            
            else:
                answer += i[j].lower()
                
        answer += ' '
    
    return answer[0:-1]