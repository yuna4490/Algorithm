def solution(name, yearning, photo):
    answer = []
    
    dic = {}
    
    for n, y in zip(name, yearning):
        dic[n] = y
    
    for i in photo:
        num = 0
        for j in i:
            if j in dic.keys():
                num += dic[j]
        
        answer.append(num)
            
    return answer