def solution(arr1, arr2):
    answer = []
    
    for a1, a2 in zip(arr1, arr2):
        answer2 = []
        for a, b in zip(a1, a2):
            answer2.append(a+b)
        
        answer.append(answer2)
            
    return answer