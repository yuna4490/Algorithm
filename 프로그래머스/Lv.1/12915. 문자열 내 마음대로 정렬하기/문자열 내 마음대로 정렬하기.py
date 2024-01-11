def solution(strings, n):
    answer = []
    dic = {}
    
    for string in strings:
        dic[string] = string[n]
    
    sorted_dic = sorted(dic.items(), key = lambda x : (x[1], x[0]))
    
    for d in sorted_dic:
        answer.append(d[0])
        
    return answer